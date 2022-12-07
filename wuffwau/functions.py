def year_handler(dog_data, dog_name, year):
    if len(year) > 0:
        return int(year)

    latest_year = max([int(row["StichtagDatJahr"]) for row in dog_data if
                       row["HundenameText"].lower() == dog_name.lower()])

    return latest_year
