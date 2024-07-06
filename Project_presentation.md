###Project Description: 
- Collecting Information about COVID-19 and vaccine using disease.sh API

###Overview:
- This is a Python project that displays data on the current COVID-19 statistics using a disease.sh API. It contains the newest data for COVID-19 cases, deaths, recovered, and testing worldwide, by continent, and by country.

###Features and Components:

# API Integration:
- The project is integrated with the disease.sh API for extracting real-time COVID-19 statistics, for more info please check: https://disease.sh/docs/#/.
 Two files are used to handle the API requests with the names vaccine_api.py and disease_api.py.
 
# Data Retrieval:
- The program retrieves all the major metrics on COVID-19, including total cases, deaths, recoveries, active cases, critical cases, cases per million, and deaths per million.
- Also, will include the vaccine information for a given country.
- The fetched information will be in JSON form handling HTTP requests.

# User Interaction
- The user inputs queries about either a specific continent or individual countries regarding COVID-19 information and the vaccine info destined for that country.

# Error Handling and Validation:
- Error Handling: The project has integrated error handling in case API requests fail for unexpected API responses.

# Documentation and Code Structure
- The code structure contains four files as below:
	*disease_api.py that defines a python class DiseaseAPI with multiple methods interacting with external API to get COVID-19 info for worldwide, all continents, one continent, all countries, one country, and make_request method.
	*vaccine_api.py that defines a python class Vaccine with multiple methods interacting with external API to get COVID-19 vaccine for one country, make_request, and display the output.
	*display_data.py that defines a python classes to display the output for COVID-19 statistics, one class will display the output for the continent “continent_info” and the other which is inherited “continent_and_country_info” to get the information about the country and its continent. 
	 Also, new methods for data visualization allow users to compare various COVID-19 metrics through bar visually
	*main.py This file is used to ask the user to enter the continent and the country to get all the information along with the chart by calling the methods 


# Deployment and Environment Management:
- Requirements.txt will be used for handling the dependencies of the project, which ensures the same working of all environments.
- Using the pip freeze command.


##Conclusion:
- This is a Python project on extracting and visualization of COVID-19  and vaccine data from the open API website “disease.sh API.
