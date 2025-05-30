"""
Title:       Critical Thinking Assignment #3
Author:      Minh Nguyen
Created:     2025-05-30
Last Edited: 2025-05-30
Description: This program helps users decide what to wear based on the current weather conditions.
            The user is prompted to input the current temperature (in Fahrenheit), the type of weather options of
            (sunny, rainy, snowy, cloudy, windy, stormy), and wind speed (in mile/h). The program validates the inputs to ensure
            they are within a reasonable range. It then converts the temperature to Celsius and uses that,
            along with weather type and wind speed, to determine a suitable outfit. The program outputs a
            personalized outfit suggestion based on the conditions.
User Input:
    - Temperature in Fahrenheit (Float)
    - Weather type (String: sunny, rainy, snowy, etc.)
    - Wind speed in mile/h (Float)
Program Output:
    - Display of the entered weather conditions (in °F)
    - Suggested outfit based on the weather and wind conditions
"""

#Function to get temp user input
def get_temperature():
    while True:
        try:
            temp_f = float(input("Enter the current temperature (in °F): "))
            if -60 <= temp_f <= 140:
                return temp_f
            else:
                print("Please enter a temperature between -60°F and 140°F.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Function to get weather type user input
def get_weather_type():
    weather_options = ["sunny", "rainy", "snowy", "cloudy", "windy", "stormy"]
    while True:
        weather_userInput = input("Enter the weather type (sunny, rainy, snowy, cloudy, windy, stormy): ").strip().lower()
        if weather_userInput in weather_options:
            return weather_userInput
        else:
            print(f"Invalid weather type. Choose from: {', '.join(weather_options)}")

#Function to get wind speed user input
def get_wind_speed():
    while True:
        try:
            wind = float(input("Enter the wind speed (in mph): "))
            if 0 <= wind <= 100:
                return wind
            else:
                print("Please enter a wind speed between 0 and 100 mph.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Display suggestion accordingly with user input
def suggest_outfit(temp_f, weather, wind_mph):
    print("\nWeather Summary:")
    print(f"Temperature: {temp_f}°F")
    print(f"Weather Type: {weather}")
    print(f"Wind Speed: {wind_mph} mph\n")

    #First conditional structure
    if temp_f < 32:
        if weather == "snowy":
            print("Suggested Outfit: Heavy coat, thermal wear, gloves, and boots.")
        else:
            print("Suggested Outfit: Warm coat, scarf, gloves, and hat.")
    elif 32 <= temp_f <= 50:
        if wind_mph > 20:
            print("Suggested Outfit: Coat, scarf, and windbreaker.")
        else:
            print("Suggested Outfit: Light jacket and warm clothes.")
    elif 51 <= temp_f <= 68:
        if weather in ["rainy", "cloudy"]:
            print("Suggested Outfit: Long-sleeve shirt and a rain jacket.")
        else:
            print("Suggested Outfit: Sweater or light jacket.")
    elif 69 <= temp_f <= 86:
        if weather == "sunny":
            print("Suggested Outfit: T-shirt, shorts, sunglasses, and sunscreen.")
        else:
            print("Suggested Outfit: Comfortable clothes with a light jacket.")
    else:
        print("Suggested Outfit: Tank top, shorts, sunglasses, and stay hydrated!")

    #Second conditional structure
    if weather == "rainy":
        print("Don't forget an umbrella!")

    #Third conditional structure
    if wind_mph > 25:
        print("It's very windy today!")

# Main
print("Welcome to the Weather-Based Outfit Advisor!")

temperature_fahrenheit = get_temperature()
weather_type = get_weather_type()
wind_speed_mph = get_wind_speed()

suggest_outfit(temperature_fahrenheit, weather_type, wind_speed_mph)
