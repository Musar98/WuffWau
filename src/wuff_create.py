import random

from dog_client import get_dog_data, download_random_dog_media
from functions import print_header, print_footer


def wuff_create(output_dir, year):
    dog_data = get_dog_data(year)

    dog_names = list(set([dog["HundenameText"] for dog in dog_data
                          if dog["HundenameText"] != "?"]))

    dog_birth_years = list(set([dog["GebDatHundJahr"] for dog in dog_data]))

    random_dog_name = random.choice(dog_names)
    random_sex = random.choice(["m", "w"])
    random_birth_year = random.choice(dog_birth_years)

    generated_file_name_and_path = download_random_dog_media(random_dog_name, random_birth_year, output_dir)

    path_information = f"The image of the new dog can be found here: {generated_file_name_and_path}"
    max_output_len = len(path_information)
    header_title = "YOU HAVE SUCCESSFULLY CREATED A NEW DOG!"

    header_create_new_dog = print_header(max_output_len, header_title)
    footer_create_new_dog = print_footer(max_output_len)

    print(f"{header_create_new_dog}\n"
          f"|| - Name: {random_dog_name} ||\n"
          f"|| - Birth year: {random_birth_year} ||\n"
          f"|| - Sex: {random_sex} ||\n"
          f"|| - {path_information} ||\n"
          f"{footer_create_new_dog}")
