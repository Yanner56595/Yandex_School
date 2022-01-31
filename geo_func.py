import requests
from io import BytesIO
from PIL import Image


def get_toponym(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()
        # Получаем первый топоним из ответа геокодера.
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        return toponym
    return None


def get_coords(toponym_to_find):
    toponym = get_toponym(toponym_to_find)
    toponym_coodrinates = toponym["Point"]["pos"]
    if toponym_coodrinates:
        return toponym_coodrinates.split()
    return None, None


def show_map(lon_lat, type_map, delta='0.005,0.005', point=None):
    if not point:
        params = {
            'll': lon_lat,
            'spn': delta,
            'l': type_map
        }
    else:
        params = {
            'll': lon_lat,
            'spn': delta,
            'l': type_map,
            'pt': point
        }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=params)

    Image.open(BytesIO(
        response.content)).show()


def get_span(toponym_to_find):
    toponym = get_toponym(toponym_to_find)
    if toponym:
        envelope = toponym['boundedBy']['Envelope']
        left, bottom = envelope['lowerCorner'].split()
        right, top = envelope['upperCorner'].split()

        dx = abs(float(left) - float(right)) / 2
        dy = abs(float(bottom) - float(top)) / 2

        span = f'{dx},{dy}'
        return span
    return None