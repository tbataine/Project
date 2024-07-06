
import requests

class DiseaseAPI: #This class will use methods to deal with an API providing data about COVID-19.
    def __init__(self):
        self.base_url = 'https://disease.sh/v3/covid-19'

    def get_all_countries(self): # This function will call the API to return data on all countries affected by COVID-19.
        endpoint = f'{self.base_url}/countries'
        return self._make_request(endpoint)

    def get_country_data(self, country): # This function will call the API to return data on one country affected by COVID-19.
        endpoint = f'{self.base_url}/countries/{country}'
        return self._make_request(endpoint)

    def get_worldwide_data(self): #This function will call the API to return global data about COVID-19.
        endpoint = f'{self.base_url}/all'
        return self._make_request(endpoint)

    def get_all_continents(self): # This function will call the API to return data for all continents affected by COVID-19 
        endpoint = f'{self.base_url}/continents'
        return self._make_request(endpoint)

    def get_continent_data(self, continent): # This function will call the API to return data on one continent affected by COVID-19.
        endpoint = f'{self.base_url}/continents/{continent}'
        return self._make_request(endpoint)

    def _make_request(self, endpoint): # This function will send an HTTP GET request to the endpoint and returns its JSON response.
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request Exception: {e}")
            return None

