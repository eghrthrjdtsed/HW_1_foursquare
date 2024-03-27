import requests
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def search_places_by_category_and_city(category, city):
    url = "https://api.foursquare.com/v3/places/search"
    headers = {
        "Accept": "application/json",
        "Authorization": os.getenv("ADDITIONAL_API_KEY")
    }
    params = {
        "query": category,
        "near": city,
        "limit": 10
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        places = response.json().get("results", [])
        if places:
            for place in places:
                name = place.get("name")
                location = place.get("location", {})
                address = location.get("address", "Адрес не указан")
                rating = place.get("rating", "Рейтинг не указан")
                print(f"Название: {name}, Адрес: {address}, Рейтинг: {rating}")
        else:
            print("По вашему запросу заведения не найдены.")
    else:
        print(f"Произошла ошибка при обращении к API. Код ошибки: {response.status_code}")


if __name__ == "__main__":
    category = input("Введите интересующую вас категорию (например, кофейня, музей, парк): ")
    city = input("Введите название города (например, Москва, Нью-Йорк): ")
    search_places_by_category_and_city(category, city)
