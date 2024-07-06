from disease_api import DiseaseAPI
from vaccine_api import Vaccine
from display_data import continent_info, continent_and_country_info
import matplotlib.pyplot as plt


def main():
    #continent= 'Europe'
    # Initialize DiseaseAPI
    # Ask the user to enter a continent name
    disease_api = DiseaseAPI()
    continent_name = input("Enter a continent name: ")
    continent_data = disease_api.get_continent_data(continent_name)
    get_continent_info= continent_info(continent_data).display()

    #Below is example to return all continents 
    """all_continents_data = disease_api.get_all_continents()
    if all_continents_data:
        print("COVID-19 Data for All Continents:")
        for continent_data in all_continents_data:
            disease = continent_info(continent_data)
            disease.display()"""

    # Ask the user to enter a country name (Jordan)
    test= DiseaseAPI()
    country_name = input("Enter a country name: ")
    country_data= test.get_country_data(country_name)
    get_info = continent_and_country_info(country_data)
    get_info.display()

   #Ask the user to enter a country name to check the vaccine infok
    vaccine_info = Vaccine()
    vaccine_country= input("Enter the country name to check the vaccine info: ")
    vaccine_info.display(vaccine_country)

    get_info.plot_cases_vs_active() # This will return total and active cases for each country using matplotlib as a bar chart
    get_info.plot_recovered_vs_dead() # This will return recovered and dead cases for each country using matplotlib as a bar chart
    get_info.plot_critical_vs_active() # This will return critical and active cases for each country using matplotlib as a bar chart
    get_info.plot_total_vs_test_per_million()# This will return total vs test_per_million for each country using matplotlib as a bar chart

    world_info = DiseaseAPI()
    print(f"The worldwide data: \n{world_info.get_worldwide_data()}")
    
if __name__ == "__main__":
    main()
