import collections
from functions import print_header, process_common_names, dog_names_by_length
from dog_client import get_dog_data


def wuff_stats():
    dog_data = get_dog_data()

    dog_names = [dog["HundenameText"] for dog in dog_data if dog["HundenameText"] != "?"]

    male_dog_names = [dog["HundenameText"] for dog in dog_data if
                      dog["HundenameText"] != "?" and dog["SexHundLang"][0] == "m"]
    female_dog_names = [dog["HundenameText"] for dog in dog_data if
                        dog["HundenameText"] != "?" and dog["SexHundLang"][0] == "w"]

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

    print_header_longest_name = print_header(max_len_dog_name, "Longest Name(s)")
    print_header_shortest_names = print_header(min_len_dog_name, "Shortest Name(s)")
    print_header_most_common_names_overall = print_header(longest_output_most_common_dog_names,
                                                          "Top 10 most common overall Dog Names")
    print_header_most_common_male_dog_names = print_header(longest_output_most_common_male_dog_names,
                                                           "Top 10 most common male Dog Names")
    print_header_most_common_female_dog_names = print_header(longest_output_most_common_female_dog_names,
                                                             "Top 10 most common female Dog Names")

    print(
        f"{print_header_longest_name}"
        f"\n{longest_names}\n"
        f"\n{print_header_shortest_names}"
        f"\n{shortest_names}\n"
        f"\n{print_header_most_common_names_overall}"
        f"\n{join_most_common_dog_names}\n"
        f"\n{print_header_most_common_male_dog_names}"
        f"\n{join_most_common_male_dog_names}\n"
        f"\n{print_header_most_common_female_dog_names}"
        f"\n{join_most_common_female_dog_names}\n")
