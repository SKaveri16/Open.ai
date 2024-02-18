import requests
from config import OPENWEATHERMAP_API_KEY

# Rest of the code remains the same


def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    if 'main' in weather_data and 'temp' in weather_data['main']:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
    else:
        print("Weather information not available.")

def main():
    city = input("Enter city name: ")
    api_key = "YOUR_API_KEY"  # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
