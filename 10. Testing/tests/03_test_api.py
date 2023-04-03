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
