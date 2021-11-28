# python_api_test
 Automation test of public API using python and pytest

API name: weather-api

API URL: https://goweather.herokuapp.com/weather/{city}

Source: https://github.com/robertoduessmann/weather-api

Test case 1: User should be able to get weather information of a given city

Test case 2: No weather infromation is displayed if given an invalid city name 

Test case 3: Error message should be returned for invalid URL

Test case 4: Error message should be returned for empty city name

# Installation steps
 - Install Python
 - Install pytest
 - Install requests
 - Clone the project 
 - Open Terminal
 - Go to the 'test' folder 
 - Execute the following command 
 - python -m pytest  