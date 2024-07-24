import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"]
        }
    else:
        return None

def main():
    api_key = "5bf5f6a7e701e983c9c40fb59dba617f"  # Replace with your actual API key
    location = input("Enter the city name or ZIP code: ")
    weather_data = get_weather(api_key, location)
    if weather_data:
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Weather: {weather_data['weather']}")
    else:
        print("Failed to get weather data. Please check the location and try again.")

if __name__ == "__main__":
    main()
