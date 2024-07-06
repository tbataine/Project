import matplotlib.pyplot as plt

class continent_info: #class country_info: # Class to store information about a country COVID-19 statistics.
    def __init__(self, continent_data):
        self.country_data = continent_data.get('continent')
        self.cases = continent_data.get('cases')
        self.deaths = continent_data.get('deaths')
        self.recovered = continent_data.get('recovered')
    
    def display(self): # prints out the attributes of the Continent 
        print(f"Continent: {self.country_data}")
        print(f"Total Cases: {self.cases}")
        print(f"Recovered Cases: {self.recovered}")
        print(f"Deaths: {self.deaths}")
        print("")

class continent_and_country_info(continent_info):  # class inherits from continent_info It extends country_info by adding additional attributes
    def __init__(self, country_data):
        super().__init__(country_data)
        self.country= country_data.get('country')
        self.cases = country_data.get('cases')
        self.deaths = country_data.get('deaths')
        self.recovered = country_data.get('recovered')
        self.active = country_data.get('active')
        self.critical = country_data.get('critical')
        self.cases_per_million = country_data.get('casesPerOneMillion')
        self.deaths_per_million = country_data.get('deathsPerOneMillion')
        self.total_tests = country_data.get('tests')
        self.tests_per_million = country_data.get('testsPerOneMillion')

    def display(self):
        super().display()
        print(f"Country: {self.country}" )
        print(f"Total Cases: {self.cases}")
        print(f"Recovered Cases: {self.recovered}")
        print(f"Deaths: {self.deaths}")
        print(f"Active Cases: {self.active}" )
        print(f"Critical Cases: {self.critical}")
        print(f"Cases Per Million: {self.cases_per_million}")
        print(f"Deaths Per Million: {self.deaths_per_million}")
        print(f"Total Tests: {self.total_tests}")
        print(f"Tests Per Million: {self.tests_per_million}")
        print("")
    # Below are methods to generate and display different types of plots
    def plot_recovered_vs_dead(self): 
        labels = ['Recovered', 'Deaths']
        values = [self.recovered, self.deaths]
        colors = ['lightgreen', 'lightcoral']

        plt.figure(figsize=(7, 7))
        plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title(f'Recovered VS Deaths {self.country}')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

    def plot_critical_vs_active(self):
        labels = ['Critical', 'Active']
        values = [self.critical, self.active]
        colors = ['red', 'blue']

        plt.figure(figsize=(7, 7))
        plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title(f'Critical VS Active in {self.country}')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

    def plot_cases_vs_active(self):
        labels = ['Cases', 'Active Cases']
        values = [self.cases, self.active]
        colors = ['blue', 'orange']

        plt.figure(figsize=(7, 7))
        plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title(f'Cases vs Active Cases in {self.country}')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

    def plot_total_vs_test_per_million(self): 
        labels = ['Total Tests', 'Tests per Million']
        values = [self.total_tests, self.tests_per_million]
        colors = ['lightgreen', 'lightcoral']

        plt.figure(figsize=(7, 7))
        plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title(f'Total Tests vs Tests per Million {self.country}')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()
