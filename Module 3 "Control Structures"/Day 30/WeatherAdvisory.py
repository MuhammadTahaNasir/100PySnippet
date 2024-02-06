def weather_forecaster():
    print("Welcome to the Weather Forecaster!")
    temperature = float(input("Enter the current temperature (in Celsius): "))
    humidity = float(input("Enter the current humidity (in percentage): "))
    wind_speed = float(input("Enter the current wind speed (in km/h): "))                      

    if temperature > 25:
        print("It's hot outside. Wear light clothes and stay hydrated.")
        if humidity > 70:
            print("It's also humid. Consider staying indoors if possible.")
    elif temperature < 10:
        print("It's cold outside. Wear warm clothes and consider carrying an umbrella.")
    else:
        print("The weather is moderate. Enjoy your day!")

    if wind_speed > 20:  
        print("It's windy outside. Hold onto your hats!")

if __name__ == "__main__":
    weather_forecaster()
