import requests
import json
import time

class TaskAutomation:
    def __init__(self):
        self.api_key = 'YOUR_API_KEY'
        self.api_endpoint = 'https://api.example.com'
    
    def send_request(self, endpoint, payload):
        headers = {'Authorization': 'Bearer ' + self.api_key, 'Content-Type': 'application/json'}
        response = requests.post(self.api_endpoint + endpoint, headers=headers, json=payload)
        return response.json()
    
    def automate_task(self, task):
        if task == 'email':
            email_subject = 'Hello from Spxing AI!'
            email_content = 'This is an automated email sent by Spxing AI.'
            payload = {
                'subject': email_subject,
                'content': email_content,
                'recipient': 'example@example.com'
            }
            response = self.send_request('/email/send', payload)
            if response['success']:
                print('Email sent successfully!')
            else:
                print('Failed to send email.')
        
        elif task == 'weather':
            payload = {'location': 'New York'}
            response = self.send_request('/weather/get', payload)
            if response['success']:
                weather_data = response['data']
                print('Current weather in New York:')
                print('Temperature:', weather_data['temperature'])
                print('Condition:', weather_data['condition'])
            else:
                print('Failed to retrieve weather information.')
        
        elif task == 'stock_prices':
            payload = {'symbols': ['AAPL', 'GOOGL', 'MSFT']}
            response = self.send_request('/stocks/prices', payload)
            if response['success']:
                stock_prices = response['data']
                print('Current stock prices:')
                for symbol, price in stock_prices.items():
                    print(symbol, ':', price)
            else:
                print('Failed to retrieve stock prices.')
        
        else:
            print('Unsupported task:', task)
    
    def schedule_task(self, task, delay_seconds):
        print('Scheduling task:', task, 'with a delay of', delay_seconds, 'seconds.')
        time.sleep(delay_seconds)
        self.automate_task(task)
