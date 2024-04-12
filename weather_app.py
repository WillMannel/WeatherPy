# weather_app.py
from api_handler import get_weather

def main():
    print("Welcome to the Python Weather App!")
    city = input("Enter the city name: ")
    weather_data = get_weather(city)
    
    if weather_data["cod"] != "404":
        main_info = weather_data["main"]
        temperature = main_info["temp"]
        pressure = main_info["pressure"]
        humidity = main_info["humidity"]
        weather_desc = weather_data["weather"][0]["description"]
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_desc}")
    else:
        print(f"City {city} not found!")

if __name__ == "__main__":
    main()
