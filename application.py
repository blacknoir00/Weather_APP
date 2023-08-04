from flask import Flask, request, jsonify, render_template
import requests

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/weather')
def get_weather():
    location = request.args.get('location')
    api_key = 'dd7f41c4b8f20b4512b68981d37a7b2a'
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'

    try:
        response = requests.get(weather_url)
        weather_data = response.json()
        return jsonify(weather_data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

if __name__ == '__main__':
    application.run()
