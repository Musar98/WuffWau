import csv
import pathlib
import shutil
import sys

import requests as req

from constants import request_error, req_err_header, req_err_footer, current_dir
from functions import year_handler


def get_dog_data(year):
    dog_data_url = "https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen_od1002/download/KUL100OD1002.csv"
    try:
        dog_data = req.get(dog_data_url)

    except req.RequestException:
        print(f"{req_err_header}")
        sys.exit(f"|| - {request_error} ||\n"
                 f"{req_err_footer}")

    decoded_and_split_dog_data = dog_data.content.decode("utf-8-sig").splitlines()

    dog_data_csv_reader = csv.DictReader(decoded_and_split_dog_data)

    dog_data_as_list = list(dog_data_csv_reader)

    year = year_handler(dog_data_as_list, year)

    dog_data_for_year = [dog for dog in dog_data_as_list if int(dog["StichtagDatJahr"]) == year]

    return dog_data_for_year


def download_random_dog_media(dog_name, birth_year, output_dir):
    if not output_dir:
        output_dir = current_dir

    if output_dir != current_dir:
        output_dir = pathlib.Path(output_dir)

    try:
        random_dog_media = req.get("https://random.dog/woof.json")

    except req.RequestException:
        print(f"{req_err_header}")
        sys.exit(f"|| - {request_error} ||\n"
                 f"{req_err_footer}")

    random_dog_media_as_json = random_dog_media.json()

    download_url = random_dog_media_as_json["url"]
    file_name_only = download_url.split("https://random.dog/")[1]
    file_extension = file_name_only.split(".")[1]

    file_path_and_name = f"{output_dir}/{dog_name}_{birth_year}.{file_extension}"

    try:
        download_response = req.get(download_url, stream=True)

    except req.RequestException:
        print(f"{req_err_header}")
        sys.exit(f"|| - {request_error} ||\n"
                 f"{req_err_footer}")

    try:
        with open(file_path_and_name, 'wb') as new_dog_file:
            shutil.copyfileobj(download_response.raw, new_dog_file)
        del download_response
    except FileNotFoundError:
        sys.exit(f"Can not find the specified directory: {output_dir}\n"
                 f"Please make sure you have entered a valid directory.")

    return file_path_and_name
