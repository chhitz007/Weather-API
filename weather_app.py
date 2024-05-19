import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    api_key = 'fd1d9069bb10217b4b1f3202adf0ee1f'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        # print(data)          --->   just to check 

        
        return render_template('index.html', city=city, temperature=data['main']['temp'], humidity=data['main']['humidity'], pressure=data['main']['pressure'], temp_min=data['main']['temp_min'], temp_max=data['main']['temp_max'])

    except requests.exceptions.RequestException as e:
        # Handle request exceptions (e.g., network issues, invalid URL, etc.)
        return render_template('error.html', error_message=str(e))

    except Exception as e:
        # Handle other unexpected exceptions
        return render_template('error.html', error_message='An unexpected error occurred.')

if __name__ == '__main__':
    app.run(debug=True)