from dog_data import get_dog_data
from functions import year_handler


def find_dog(dog_name, year):
    dog_data = get_dog_data()

    year = year_handler(dog_name, year)

    dog_search_results = [f"{row['HundenameText']} {row['GebDatHundJahr']} {row['SexHundLang'][0]}"
                          for row in dog_data
                          if row["HundenameText"].lower() == dog_name.lower()
                          and int(row["StichtagDatJahr"]) == year]

    for dog in dog_search_results:
        print(dog)
