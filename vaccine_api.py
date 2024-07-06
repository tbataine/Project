import requests

class Vaccine: #This class is to implement methods for getting COVID-19 vaccines data from an API.
    def __init__(self):
        self.base_url = 'https://disease.sh/v3/covid-19'
        
    def get_vaccine_data(self, country): # This function would fetch Covid-19 vaccine coverage data specific to one country.
        endpoint = f'{self.base_url}/vaccine/coverage/countries/{country}?lastdays=1&fullData=true'
        return self._make_request(endpoint)
    
    def display(self, country):
        vaccine_data = self.get_vaccine_data(country)
        if vaccine_data:
            print(f"Vaccine data for {country}:")
            print(vaccine_data)
            print("")
        else:
            print(f"No vaccine data available for {country}")

    def _make_request(self, endpoint): # This function will send an HTTP GET request to the endpoint and returns its JSON response.
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request Exception: {e}")
            return None


        
        