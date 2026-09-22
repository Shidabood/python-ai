import requests

def get_weather(latitude, longtitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longtitude}&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data


get_weather(48.85, 2.35)