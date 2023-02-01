# DSC 510
# Week 12
# Programming Assignment 12 Week 12
# Author Kiran Komati
# 02/20/2021
# Description: This program uses request library to get weather data from OpenWeatherMap
# based on the city or zip code that user enters at the prompt and displays it back to the user

# Change#: 0
# Change(s) Made:
# Date of Change:
# Author:
# Date Moved to Production:


import requests
import sys


# user-defined exception if zip has more than 5 digits
class ZipError(Exception):
    pass


def getWeather(WeatherURL):
    try:
        response = requests.get(WeatherURL)
    except requests.HTTPError as exception:
        print("Error while retrieving data. Please check city/zip entered.")
    else:
        if response.status_code == 200:
            weather_dictionary = response.json()
            prettyprint(weather_dictionary)
        elif response.status_code == 404:
            print("City not found. Please check.")
        elif response.status_code == 400:
            print("Invalid zipcode. Please check.")
        else:
            print(response.status_code)
            print("Please enter a valid city/zip.")


def prettyprint(weather_dictionary):
    try:
        weatherinfo = weather_dictionary["main"]
        cloudinfo = weather_dictionary["weather"]
        cityname = weather_dictionary["name"]
        temp = weatherinfo["temp"]
        temp_max = weatherinfo["temp_max"]
        temp_min = weatherinfo["temp_min"]
        pressure = weatherinfo["pressure"]
        humidity = weatherinfo["humidity"]
        cloud_desc = cloudinfo[0]["description"]
        print(cloudinfo[0])
    except KeyError:
        print("Key value not found")
    else:
        print("\nCurrent Weather Conditions For {}".format(cityname))
        print("Current Temp: {} degrees".format(temp))
        print("High Temp: {} degrees".format(temp_max))
        print("Low Temp: {} degrees".format(temp_min))
        print("Pressure: {} hPa".format(pressure))
        print("Humidity: {}%".format(humidity))
        print("Cloud Cover: {}".format(cloud_desc))


def main():
    print("Welcome to Weather Application")
    WeatherAPIKey = 'ec049808f70141a1830a99045a5985a3'
    baseURL = "http://api.openweathermap.org/data/2.5/weather?"
    proceed = 'y'
    while proceed.lower() == 'y':
        LookupType = input("\nWould you like to lookup weather data by US City or zip code? Enter 1 for US City 2 for zip: ")

        if LookupType == '1':
            try:
                city = str(input("Please enter the city name in the format City, State, Country: "))
                if city.isnumeric():
                    print("\nPlease enter a valid city. You entered {}".format(city))
                    continue
                else:
                    RequestString = "q=" + city.lower()
            except ValueError:
                print("\nPlease enter a valid City! You entered {}".format(city))
                continue
        elif LookupType == '2':
            try:
                zipcode = int(input("Please enter the zip code: "))
                if len(str(zipcode)) > 5:
                    raise ZipError
            except ValueError:
                print("\nPlease enter a valid zip code!")
                continue
            except ZipError:
                print("\nzipcode should not contain more than 5 digits")
                continue
            else:
                RequestString = "zip=" + str(zipcode)
        else:
            print("Invalid Entry. Enter 1 or 2")
            continue

        print("\nWould you like to view temps in Fahrenheit, Celsius, or Kelvin.")
        UnitsType = input("Enter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin: ")
        if UnitsType.upper() == 'F':
            UnitsString = 'imperial'
        elif UnitsType.upper() == 'C':
            UnitsString = 'metric'
        elif UnitsType.upper() == 'K':
            UnitsString = ''
        else:
            print("Incorrect Unit entered")
            continue

        WeatherURL = baseURL + RequestString + "&appid=" + WeatherAPIKey + "&units=" + UnitsString
        getWeather(WeatherURL)
        proceed = input("\nWould you like to perform another weather lookup?(Y/N): ")
    if proceed.lower() == 'n':
        print("\nThat's all for today! Have a good rest of the day!")
    else:
        sys.exit("Invalid option selected. Exiting...")


if __name__ == "__main__":
    main()
