import requests
import datetime

from config import open_weather_token


def get_weather(city, open_weather_token):

    code_for_smile = {
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Облачно \U00002601',
        'Rain': 'Дождь \U00002614',
        'Drizzle': 'Дождь \U00002614',
        'Thunderstorm': 'Гроза \U000026A1',
        'Snow': 'Снег \U0001F328',
        'Mist': 'Туман \U0001F32B'
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        # Determining clothing based on temperature
        if cur_weather < 10:
            clothing = "Куртка, штаны и ботинки"
        else:
            clothing = "Ветровка, шорты и кроссовки"

        weather_description = data['weather'][0]['main']
        if weather_description in code_for_smile:
            wd = code_for_smile[weather_description]
        else:
            wd = "Я не знаю, сам посмотри что там"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        print(
            f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
            f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер км за годину: {wind} м/с\n'
            f'Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n'
            f'Для данной температуры рекомендуется надеть: {clothing}\nГарного дня!')

    except Exception as ex:
        print(ex)
        print('Проверьте название города')


def main():
    city = input('Введите город в котором вы находитесь. Вводите город на английском!!!: ')
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
