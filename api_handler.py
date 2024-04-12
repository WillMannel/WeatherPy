# api_handler.py
import requests
from config import api_key, base_url

def get_weather(city):
    """ Fetch weather information for the specified city """
    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"
    response = requests.get(complete_url)
    return response.json()
