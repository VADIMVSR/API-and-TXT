import folium
import random
import requests

YANDEX_GEOCODE_API_KEY = "0d997e8f-b415-4fd0-91b1-c9547916c893"

# Список городов для игры
cities = ["Москва", "Санкт-Петербург", "Казань", "Сочи"]

# Функция для получения координат города через геокодер
def get_city_coordinates(city):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    geocode_params = {
        "geocode": city,
        "format": "json",
        "apikey": YANDEX_GEOCODE_API_KEY
    }
    response = requests.get(geocode_url, params=geocode_params).json()
    try:
        point = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        coords = tuple(map(float, point.split()))
        return coords
    except (KeyError, IndexError):
        print(f"Не удалось получить координаты для города {city}")
        return None

# Функция для создания карты города в формате HTML без названия
def create_city_map(coords, filename="city_map.html"):
    # Создаем карту с заданными координатами
    city_map = folium.Map(location=[coords[0], coords[1]], zoom_start=12)

    # Добавляем маркер на карту без подписи
    folium.Marker(location=[coords[0], coords[1]]).add_to(city_map)

    # Сохраняем карту в файл
    city_map.save(filename)
    print(f"Карта города сохранена в файл {filename}")

# Функция для игры "Угадай город"
def guess_the_city():
    random.shuffle(cities)  # Перемешиваем список городов для случайного порядка

    for city in cities:
        print(f"Показывается карта города. Угадай город!")

        # Получаем координаты города
        coords = get_city_coordinates(city)
        if not coords:
            continue

        # Создаем карту города без названия
        create_city_map(coords, f"?_map.html")

        # Подождем немного перед отображением следующего города
        input("Нажмите Enter, чтобы увидеть следующий город...")

        # Угадываем город (здесь можно добавить ввод от пользователя)
        user_guess = input("Введите ваш ответ: ").strip()
        if user_guess.lower() == city.lower():
            print("Правильный ответ!")
        else:
            print(f"Неправильно! Это был {city}.")

# Запуск игры
guess_the_city()
