###Project Overview
- Python Project that fetches and displays all information regarding COVID-19 statistics and vaccine information directly from the Disease.sh API. The application offers real-time cases, deaths, recoveries, and testing of COVID19 worldwide, on each continent, and in each country.

### Features and Components 
- The application integrates with the disease.sh API to get the latest COVID-19 statistics. The following is detailed documentation of the API: https://disease.sh/docs/#/.

#### Data Retrieval
- **COVID-19 Metrics**: It returns important metrics such as: cases, deaths, recoveries, active, critical cases, cases per million, deaths per million. 
- **Vaccine Info**: Information relating to the COVID-19 vaccines distributed in various countries.
- **Data Format**: The data to be retrieved for results would be in JSON format through HTTP requests.

#### User Interaction
- The program would need user interaction through input in the form of a query about COVID-19 statistics over the continents or individual countries.

#### Error Handling and Validation
**Error Handling**: Handle API request failures; unexpected responses from the API.

#### Documentation and Code Structure
**File Structure**:
- **disease_api.py**: This implements a class, `DiseaseAPI`, which will interface with the API provided by diseases.sh. It provides methods for getting worldwide data, data specific to a continent, data specific to a country, as well as handling an HTTP request.
- **vaccine_api.py**: Class `Vaccine` for fetching and display of COVID-19 vaccines for countries.
- **display_data.py**: A program that contains classes for COVID-19 statistics. On the continent level, it is `continent_info`, and at the country level, `continent_and_country_info` derived from the former. Moreover, it contains methods for data visualization given by Matplotlib.
- **main.py**: This will be the entry point to the App. It will prompt the user for input of a continent and a country, fetch and display relevant COVID-19 statistics and vaccine information.

### Conclusion
- The Python package will make use of the API from www.disease.sh to give real-time COVID-19 and vaccine data to the user.