import csv
import shutil
import requests as req
from functions import year_handler


def get_dog_data(year):
    response = req.get(
        "https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen_od1002/download/KUL100OD1002.csv")

    decoded_and_split_dog_data = response.content.decode("utf-8-sig").splitlines()

    dog_data_csv_reader = csv.DictReader(decoded_and_split_dog_data)

    dog_data_as_list = list(dog_data_csv_reader)

    year = year_handler(dog_data_as_list, year)

    return [dog for dog in dog_data_as_list if int(dog["StichtagDatJahr"]) == year]


def get_dog_media(dog_name, birth_year, output_dir):
    random_dog_media = req.get("https://random.dog/woof.json")
    random_dog_media_as_json = random_dog_media.json()

    download_url = random_dog_media_as_json["url"]
    file_name_only = download_url.split("https://random.dog/")[1]
    file_extension = file_name_only.split(".")[1]

    file_path_and_name = f"{output_dir}/{dog_name}_{birth_year}.{file_extension}"

    download_response = req.get(download_url, stream=True)
    with open(file_path_and_name, 'wb') as new_dog_file:
        shutil.copyfileobj(download_response.raw, new_dog_file)
    del download_response

    return file_path_and_name
