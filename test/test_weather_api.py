
import requests


def test_weather_info_api_status():
    response = requests.get("https://goweather.herokuapp.com/weather/dhaka")
    assert response.status_code == 200
    
#Test case 1: User should be able to get weather information of a given city
def test_get_weather_info_using_a_valid_city():
    #get weather information for the city "dhaka"
    response = requests.get("https://goweather.herokuapp.com/weather/dhaka").json()

    assert response["temperature"] != "", "temperature is empty"
    assert "°C" in response["temperature"] 

    assert response["wind"] != "", "Wind is empty"
    assert "km/h" in response["wind"] 

    assert response["wind"] != "", "Wind is empty"  
    assert "km/h" in response["wind"] 

    assert response["description"] != "", "Description is empty"  

    assert response["forecast"] != "", "Forcast is empty"  
    assert len(response["forecast"]) == 3

    assert response["forecast"][0]["day"] != "", "Day is empty"  
    assert response["forecast"][0]["temperature"] != "", "temperature is empty"  
    assert response["forecast"][0]["wind"] != "", "wind is empty"  


#Test case 2: No weather infromation is displayed if given an invalid city name 
def test_weather_info_using_invalid_city_name():
    response = requests.get("https://goweather.herokuapp.com/weather/invalidcity").json()

    assert response["temperature"] == "", "temperature is not empty"
    assert "°C" not in response["temperature"] 

    assert response["wind"] == "", "Wind is not empty"
    assert "km/h" not in response["wind"] 

    assert response["description"] == "", "Description is not empty"  

    assert response["forecast"] != "", "Forecast is not empty"  
    assert len(response["forecast"]) == 3

    assert response["forecast"][0]["day"] == "", "Day is not empty"  
    assert response["forecast"][0]["temperature"] == "", "temperature is not empty"  
    assert response["forecast"][0]["wind"] == "", "wind is not empty"  


#Test case 3: Error message is displayed for invalid URL
def test_get_weather_info_using_invalid_url():
    response = requests.get("https://goweather.herokuapp.com/weather_1/dhaka")
    assert response.status_code == 404

#Test case 4: Error message is displayed for empty city name

def test_get_weather_info_using_invalid_url():
    response = requests.get("https://goweather.herokuapp.com/weather/")
    assert response.status_code == 404

