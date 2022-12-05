import csv
import requests as req


def get_dog_data():
    response = req.get(
        "https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen_od1002/download/KUL100OD1002.csv")

    decoded_and_split_dog_data = response.content.decode("utf-8-sig").splitlines()

    dog_data_csv_reader = csv.DictReader(decoded_and_split_dog_data, fieldnames=["StichtagDatJahr",
                                                                                 "HundenameText",
                                                                                 "GebDatHundJahr",
                                                                                 "SexHundCd",
                                                                                 "SexHundLang",
                                                                                 "SexHundSort",
                                                                                 "AnzHunde"])

    return dog_data_csv_reader
