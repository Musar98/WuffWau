import collections

from dog_client import get_dog_data
from functions import print_header, print_footer, process_common_names, dog_names_by_length


def wuff_stats(year):
    dog_data = get_dog_data(year)

    dog_names = [dog["HundenameText"] for dog in dog_data if
                 dog["HundenameText"] != "?"]

    male_dog_names = [dog["HundenameText"] for dog in dog_data if
                      dog["HundenameText"] != "?"
                      and dog["SexHundLang"][0] == "m"]

    female_dog_names = [dog["HundenameText"] for dog in dog_data
                        if dog["HundenameText"] != "?"
                        and dog["SexHundLang"][0] == "w"]

    amt_male_dogs = len(
        [dog for dog in dog_data if dog["SexHundLang"][0] == "m"])
    amt_female_dogs = len(
        [dog for dog in dog_data if dog["SexHundLang"][0] == "w"])

    raw_most_common_dog_names_overall = collections.Counter(dog_names).most_common(10)
    raw_most_common_male_dog_names = collections.Counter(male_dog_names).most_common(10)
    raw_most_common_female_dog_names = collections.Counter(female_dog_names).most_common(10)

    processed_most_common_names_overall = process_common_names(raw_most_common_dog_names_overall)

    processed_most_common_male_dog_names = process_common_names(raw_most_common_male_dog_names)

    processed_most_common_female_dog_names = process_common_names(raw_most_common_female_dog_names)

    join_most_common_dog_names = "\n".join(processed_most_common_names_overall["names_and_occurrences"])
    join_most_common_male_dog_names = "\n".join(processed_most_common_male_dog_names["names_and_occurrences"])
    join_most_common_female_dog_names = "\n".join(processed_most_common_female_dog_names["names_and_occurrences"])

    longest_output_most_common_dog_names = processed_most_common_names_overall["longest_output"]

    longest_output_most_common_male_dog_names = processed_most_common_male_dog_names["longest_output"]

    longest_output_most_common_female_dog_names = processed_most_common_female_dog_names["longest_output"]

    max_len_dog_name = max([len(dog_name) for dog_name in dog_names])
    min_len_dog_name = min([len(dog_name) for dog_name in dog_names])

    longest_names = dog_names_by_length(dog_names, max_len_dog_name)
    shortest_names = dog_names_by_length(dog_names, min_len_dog_name)

    header_longest_name = print_header(max_len_dog_name, "LONGEST NAME(S)")
    header_shortest_names = print_header(min_len_dog_name, "SHORTEST NAME(S)")
    header_most_common_names_overall = print_header(longest_output_most_common_dog_names,
                                                    "TOP 10 MOST COMMON OVERALL DOG NAMES")
    header_most_common_male_dog_names = print_header(longest_output_most_common_male_dog_names,
                                                     "TOP 10 MOST COMMON MALE DOG NAMES")
    header_most_common_female_dog_names = print_header(longest_output_most_common_female_dog_names,
                                                       "TOP 10 MOST COMMON FEMALE DOG NAMES")

    male_v_female_dogs_msg = f"There are {amt_male_dogs} male dogs and {amt_female_dogs} female dogs!"

    header_male_v_female = print_header(len(male_v_female_dogs_msg), "MALE VS FEMALE DOGS")
    footer_male_v_female = print_footer(len(male_v_female_dogs_msg))

    footer_longest_name = print_footer(max_len_dog_name)
    footer_shortest_name = print_footer(min_len_dog_name)
    footer_overall = print_footer(longest_output_most_common_dog_names)
    footer_male = print_footer(longest_output_most_common_male_dog_names)
    footer_female = print_footer(longest_output_most_common_female_dog_names)

    print(
        f"{header_longest_name}"
        f"\n{longest_names}\n"
        f"{footer_longest_name}\n"
        f"\n{header_shortest_names}"
        f"\n{shortest_names}\n"
        f"{footer_shortest_name}\n"
        f"\n{header_most_common_names_overall}"
        f"\n{join_most_common_dog_names}\n"
        f"{footer_overall}\n"
        f"\n{header_most_common_male_dog_names}"
        f"\n{join_most_common_male_dog_names}\n"
        f"{footer_male}\n"
        f"\n{header_most_common_female_dog_names}"
        f"\n{join_most_common_female_dog_names}\n"
        f"{footer_female}\n"
        f"\n{header_male_v_female}\n"
        f"|| - {male_v_female_dogs_msg} ||\n"
        f"{footer_male_v_female}\n")
