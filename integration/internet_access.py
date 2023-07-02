import requests
import urllib.parse
from bs4 import BeautifulSoup
import random
import re
import webbrowser

class InternetAccess:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        }

    def search_on_google(self, query):
        encoded_query = urllib.parse.quote(query)
        url = f'https://www.google.com/search?q={encoded_query}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.find_all('div', class_='tF2Cxc')
            if search_results:
                result_text = search_results[0].get_text()
                return result_text
        return "Sorry, I couldn't find any relevant information."

    def get_random_fact(self):
        url = 'https://www.thefactsite.com/random-facts/'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            facts = soup.find_all('div', class_='entry-content')
            if facts:
                random_fact = random.choice(facts).get_text()
                return random_fact
        return "Unable to retrieve a random fact at the moment."

    def get_weather(self, city):
        api_key = 'YOUR_WEATHER_API_KEY'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            weather_data = response.json()
            if 'main' in weather_data and 'weather' in weather_data:
                description = weather_data['weather'][0]['description']
                temp = weather_data['main']['temp']
                return f"The weather in {city} is {description} with a temperature of {temp}°C."
        return f"Sorry, I couldn't fetch the weather for {city}."

    def get_news(self):
        url = 'https://news.google.com/'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            news_items = soup.find_all('h3', class_='ipQwMb ekueJc RD0gLb')
            if news_items:
                news_list = [item.get_text() for item in news_items]
                return news_list
        return "Unable to fetch the latest news at the moment."

    def search_images(self, query, num_images=5):
        encoded_query = urllib.parse.quote(query)
        url = f'https://www.google.com/search?tbm=isch&q={encoded_query}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            image_links = soup.find_all('img', class_='t0fcAb')
            if image_links:
                image_urls = [img['src'] for img in image_links]
                return random.sample(image_urls, num_images)
        return "No images found for the given query."

    def open_website(self, url):
        webbrowser.open(url)

    def search_videos(self, query):
        encoded_query = urllib.parse.quote(query)
        url = f'https://www.youtube.com/results?search_query={encoded_query}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            video_ids = re.findall(r'watch\?v=(\S{11})', response.text)
            if video_ids:
                video_links = [f'https://www.youtube.com/watch?v={video_id}' for video_id in video_ids]
                return video_links
        return "No videos found for the given query."
