from dog_data import get_dog_data


def year_handler(dog_name, year):
    dog_data = get_dog_data()

    if len(year) > 0:
        return int(year)

    latest_year = max([int(row["StichtagDatJahr"]) for row in dog_data if
                       row["HundenameText"].lower() == dog_name.lower()])

    return latest_year
