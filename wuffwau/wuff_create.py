import random

from dog_client import get_dog_data, get_dog_media
from functions import print_header


def wuff_create(output_dir):
    dog_data = get_dog_data()
    dog_names = list(set([dog["HundenameText"] for dog in dog_data if dog["HundenameText"] != "?"]))
    dog_birth_years = list(set([dog["GebDatHundJahr"] for dog in dog_data]))
    random_dog_name = random.choice(dog_names)
    random_sex = random.choice(["m", "w"])
    random_birth_year = random.choice(dog_birth_years)

    generated_file_name_and_path = get_dog_media(random_dog_name, random_birth_year, output_dir)

    max_output_len = len(f"The image of the new dog can be found here: {generated_file_name_and_path}")
    header_title = "You have successfully created a new dog!"

    print_header_create_new_dog = print_header(max_output_len, header_title)

    print(f"{print_header_create_new_dog}\n"
          f"|| - Name: {random_dog_name} ||\n"
          f"|| - Birth year: {random_birth_year} ||\n"
          f"|| - Sex: {random_sex} ||\n"
          f"|| - The image of the new dog can be found here: {generated_file_name_and_path} ||")
