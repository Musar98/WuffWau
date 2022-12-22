from dog_client import get_dog_data
import functions


def wuff_stats(year):
    dog_data = get_dog_data(year)

    dog_names = [dog["HundenameText"] for dog in dog_data if dog["HundenameText"] != "?"]

    amt_male_dogs = len([dog for dog in dog_data if dog["SexHundLang"][0] == "m"])
    amt_female_dogs = len([dog for dog in dog_data if dog["SexHundLang"][0] == "w"])

    most_common_names = functions.get_most_common_names(dog_data, dog_names)
    print_msg_most_common_names = functions.build_most_common_names_msg(most_common_names)

    max_len_dog_name = max([len(dog_name) for dog_name in dog_names])
    min_len_dog_name = min([len(dog_name) for dog_name in dog_names])

    longest_names = functions.dog_names_by_length(dog_names, max_len_dog_name)
    shortest_names = functions.dog_names_by_length(dog_names, min_len_dog_name)

    header_longest_name = functions.print_header(max_len_dog_name, "LONGEST NAME(S)")
    header_shortest_names = functions.print_header(min_len_dog_name, "SHORTEST NAME(S)")

    male_vs_female_dogs_msg_body = f"There are {amt_male_dogs} male dogs and {amt_female_dogs} female dogs!"

    male_vs_female_dogs_msg = functions.print_msg_builder("MALE VS FEMALE DOGS", male_vs_female_dogs_msg_body)

    footer_longest_name = functions.print_footer(max_len_dog_name)
    footer_shortest_name = functions.print_footer(min_len_dog_name)

    print(
        f"{header_longest_name}"
        f"\n{longest_names}\n"
        f"{footer_longest_name}\n"
        f"\n{header_shortest_names}"
        f"\n{shortest_names}\n"
        f"{footer_shortest_name}\n"
        f"{print_msg_most_common_names}"
        f"\n{male_vs_female_dogs_msg}\n"
    )
