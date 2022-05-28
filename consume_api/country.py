# Make rest api call to the https://restcountries.com/v3.1/all [gives all the list of the countries for demo purposes]

# In python we can make API call we can use requests 
# to install : python -m pip install requests
# import requests and make a call

from urllib import response
import requests

country_api_list = 'https://restcountries.com/v3.1/all'

response = requests.get(country_api_list)
country_json = response.json()

for country in country_json:
    print('Country name = ', (country['name'].get('common')), ', Area = ', country['area'], ', Population = ', country['population'])