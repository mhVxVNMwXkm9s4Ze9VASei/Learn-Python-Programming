# tests/test_api.py
import re
from unittest.mock import patch, mock_open, call
import pytest
from api import is_valid, export, write_csv

@pytest.fixture
def min_user():
	"""Represents a valid user with minimal data."""
	return {
		'email': 'minimal@example.com',
		'name': 'Primus Minimus',
		'age': 18
	}

@pytest.fixture
def full_user():
	"""Represents a valid user with full data."""
	return {
		'email': 'full@example.com',
		'name': 'Maximus Plenus',
		'age': 65,
		'role': 'emperor'
	}

@pytest.fixture
def users(min_user, full_user):
	"""List of users, two valid and one invalid."""
	bad_user = {
		'email': 'invalid@example.com',
		'name': 'Horribilis'
	}
	return [min_user, bad_user, full_user]

class TestIsValid:
	"""Test how code verifies whether a user is valid or not."""

	def test_minimal(self, min_user):
		assert is_valid(min_user)

	def test_full(self, full_user):
		assert is_valid(full_user)

	@pytest.mark.parametrize('age', range(18))
	def test_invalid_age_too_young(self, age, min_user):
		min_user['age'] = age
		assert not is_valid(min_user)

	@pytest.mark.parametrize('age', range(66, 100))
	def test_invalid_age_too_old(self, age, min_user):
		min_user['age'] = age
		assert not is_valid(min_user)

	@pytest.mark.parametrize('age', ['NaN', 3.1415, None])
	def test_invalid_age_wrong_type(self, age, min_user):
		min_user['age'] = age
		assert not is_valid(min_user)

	@pytest.mark.parametrize('age', range(18, 66))
	def test_valid_age(self, age, min_user):
		min_user['age'] = age

		assert is_valid(min_user)

	@pytest.mark.parametrize('field', ['email', 'name', 'age'])
	def test_mandatory_fields(self, field, min_user):
		del min_user[field]
		assert not is_valid(min_user)

	@pytest.mark.parametrize('field', ['email', 'name', 'age'])
	def test_mandatory_fields_empty(self, field, min_user):
		min_user[field] = ''
		assert not is_valid(min_user)

	def test_name_whitespace_only(self, min_user):
		min_user['name'] = ' \n\t'
		assert not is_valid(min_user)

	@pytest.mark.parametrize(
		'email',
		'outcome',
		[
			('missing_at.com', False),
			('@missing_start.com', False),
			('missing_end@', False),
			('missing_dot@example', False),
			('good.one@example.com', True),
			('δοκιμή@παράδειγμα.δοκιμή', True),
			('аджай@экзампл.рус', True),
		]
	)
	def test_email(self, email, outcome, min_user):
		min_user['email'] = email
		assert is_valid(min_user) == outcome

	@pytest.mark.parametrize(
		'field',
		'value',
		[
			('email', None),
			('email', 3.1415),
			('email', {}),
			('name', None),
			('name', 3.1415),
			('name', {}),
			('role', None),
			('role', 3.1415),
			('role', {}),
		]
	)
	def test_invalid_types(self, field, value, min_user):
		min_user[field] = value
		assert not is_valid(min_user)

class TestExport:
	"""Test the behavior of the 'export' function."""

	@pytest.fixture
	def csv_file(self, tmp_path):
		"""
		Yield a filename in a temporary folder.
		Due to how pytest 'tmp_path' fixture works, the file
		does not exist yet.
		"""
		yield tmp_path / "out.csv"

	@pytest.fixture
	def existing_file(self, tmp_path):
		"""Create a temporary file and put some content in it."""
		existing = tmp_path / 'existing.csv'
		existing.write_text('Please leave me alone...')
		yield existing