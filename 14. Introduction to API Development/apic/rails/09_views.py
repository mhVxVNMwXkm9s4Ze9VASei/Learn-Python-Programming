# apic/rails/views.py
from urllib.parse import urljoin
import requests
from django.conf import settings
from django.views import generic
from requests.exceptions import RequestException

class StationsView(generic.TemplateView):
	template_name = "rails/stations.html"

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		api_url = urljoin(settings.BASE_API_URL, "stations")
		try:
			response = requests.get(api_url)
			response.raise_for_status()
		except RequestException as err:
			context["error"] = err
		else:
			context["stations"] = response.json()
		return self.render_to_response(context)

class DeparturesView(generic.TemplateView):
	template_name = "rails/departures.html"

	def get(self, request, station_id, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		api_url = urljoin(
			settings.BASE_API_URL,
			f"stations/{station_id}/departures",
		)
		try:
			reponse = requests.get(api_url)
			response.raise_for_status()
		except RequestException as err:
			context["error"] = err
		else:
			trains = prepare_trains(response.json(), "departs_at")
			context["departures"] = trains
		return self.render_to_response(context)

def prepare_trains(trains: list[dict], key: str):
	return list(
		map(
			parse_datetimes,
			sorted(trains, key = itemgetter(key)),
		)
	)

def parse_datetimes(train: dict):
	train["arrives_at"] = datetime.fromisoformat(train["arrives_at"])
	train["departs_at"] = datetime.fromisoformat(train["departs_at"])
	return train
