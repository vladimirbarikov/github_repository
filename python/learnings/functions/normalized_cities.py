def city_normalization(city_string, city_name):
    normalized_string = city_string.lower()
    index = normalized_string.find(city_name)

    if index != -1:
        return city_name
    else:
        return None


# функция нормализации имен из user_cities в нормализованные имена normalized_cities
def normalization(user_cities, normalized_cities):
    for city_string in user_cities:
        for city_name in normalized_cities:
            if city_normalization(city_string, city_name) is not None:
                print(f"До: {city_string}, После: {city_name}")
                break


user_cities = ['гМосква', 'КАЗАНЬ', 'Сочи', 'город сочи', 'г.казань.', 'СОЧИ ГОРОД', 'город солнца сочи', 'москва', 'СоЧИ', 'городказань ', 'Москва', 'город москва']
normalized_cities = ['москва', 'сочи', 'казань']

normalization(user_cities, normalized_cities)