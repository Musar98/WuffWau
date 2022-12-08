from dog_client import get_dog_data
from functions import print_header, print_footer


def find_dog(dog_name, year):
    dog_data = get_dog_data(year)

    dog_search_results = [f"|| - {dog['HundenameText']} {dog['GebDatHundJahr']} {dog['SexHundLang'][0]} ||"
                          for dog in dog_data
                          if dog["HundenameText"].lower() == dog_name.lower()]

    results_as_string = "\n".join(dog_search_results)

    # - 8 is to remove the amt of special chars,
    # this is done because in this case they are easy to count manually
    output_length = len(dog_search_results[0]) - 8

    header_results = print_header(output_length, "Search Results")
    footer_results = print_footer(output_length)

    print(f"{header_results}\n"
          f"{results_as_string}\n"
          f"{footer_results}")
