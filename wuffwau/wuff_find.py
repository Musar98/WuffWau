from dog_data import get_dog_data


def find_dog(dog_name):
    dog_data = get_dog_data()
    search_dog_in_data = [row for row in dog_data if row["HundenameText"].lower() == dog_name.lower()]
    for i in search_dog_in_data:
        print(i)