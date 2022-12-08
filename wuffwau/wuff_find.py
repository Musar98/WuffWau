from dog_data import get_dog_data
from functions import year_handler


def find_dog(dog_name, year):
    dog_data = get_dog_data()

    year = year_handler(dog_data, dog_name, year)

    dog_search_results = [f"{dog['HundenameText']} {dog['GebDatHundJahr']} {dog['SexHundLang'][0]}"
                          for dog in dog_data
                          if dog["HundenameText"].lower() == dog_name.lower()
                          and int(dog["StichtagDatJahr"]) == year]

    for dog in dog_search_results:
        print(dog)
