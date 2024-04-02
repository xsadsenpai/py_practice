import requests

def get_weather(api_key, latitude, longitude):
    url = f"https://api.tomorrow.io/v4/timelines?location={latitude},{longitude}&fields=temperature,weatherCode,windSpeed&apikey={api_key}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data['data']['timelines'][0]['intervals'][0]['values']['temperature']
        weather_code = data['data']['timelines'][0]['intervals'][0]['values']['weatherCode']
        wind_speed = data['data']['timelines'][0]['intervals'][0]['values']['windSpeed']

        print(f"Температура: {temperature}°C")
        print(f"Код погоды: {weather_code}")
        print(f"Скорость ветра: {wind_speed} м/с")
    else:
        print("Не удалось получить данные о погоде.")

# Введите ваш API-ключ от Tomorrow.io
api_key = "U6dNQdl5a0X3mMYRuY26NGJYjvqHZR0z"
# Укажите координаты города Екатеринбург, Россия
latitude = "56.838011"
longitude = "60.597465"

get_weather(api_key, latitude, longitude)
