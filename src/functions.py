import collections
import sys
import constants


def year_handler(dog_data, year):
    years_with_available_data = [int(row["StichtagDatJahr"]) for row in dog_data]
    max_year = max(years_with_available_data)
    min_year = min(years_with_available_data)
    valid_years_msg = f"Please choose a year between {min_year} and {max_year} (both inclusive)"
    error_msg = print_msg_builder("ERROR", "The year must be a positive integer!")
    no_data_available_msg = print_msg_builder("NO DATA",
                                              f"Unfortunately, there is no data available for the year: {year}",
                                              valid_years_msg)

    if year == "default":
        print(
            f"\nINFO: No year [-y || --year] was provided, "
            f"the data got filtered by the latest year with available data ({max_year}) !\n")
        return max_year

    try:
        year = int(year)

    except ValueError:
        sys.exit(error_msg)

    if min_year <= year <= max_year:
        return year

    elif year < 0:
        sys.exit(error_msg)

    sys.exit(no_data_available_msg)


def print_header(output_length, title):
    title_length = len(title)

    # pipes/stars at start and end
    amt_additional_chars = 4

    full_length = output_length + amt_additional_chars

    if title_length > full_length:
        full_length = title_length + amt_additional_chars

    amount_of_leftover_space = full_length - title_length

    if amount_of_leftover_space % 2 == 0:
        start = amount_of_leftover_space // 2
        end = amount_of_leftover_space // 2

    else:
        start = amount_of_leftover_space // 2 + 1
        end = amount_of_leftover_space // 2

    return f"**{full_length * '='}**" \
           f"\n||{start * '*'}{title}{end * '*'}||" \
           f"\n**{full_length * '='}**"


def print_footer(output_length):
    # output length has 8 additional special chars
    # here 4 are filled with "*" so +4 are left to be filled with "="
    return f"**{(output_length + 4) * '='}**"


def print_msg_builder(title, msg_body, additional_msg=""):
    header = print_header(len(msg_body), title)
    footer = print_footer(len(msg_body))

    if len(additional_msg) > 0:
        return f"{header}\n" \
               f"|| - {msg_body} ||\n" \
               f"|| - {additional_msg}  ||\n" \
               f"{footer}"

    else:
        return f"{header}\n" \
               f"|| - {msg_body} ||\n" \
               f"{footer}"


def get_most_common_names(dog_data, dog_names):
    male_dog_names = [dog["HundenameText"] for dog in dog_data
                      if dog["HundenameText"] != "?"
                      and dog["SexHundLang"][0] == "m"]

    female_dog_names = [dog["HundenameText"] for dog in dog_data
                        if dog["HundenameText"] != "?"
                        and dog["SexHundLang"][0] == "w"]

    most_common_dog_names_overall = collections.Counter(dog_names).most_common(10)
    most_common_male_dog_names = collections.Counter(male_dog_names).most_common(10)
    most_common_female_dog_names = collections.Counter(female_dog_names).most_common(10)

    names_and_occurs_overall = [f"|| - Name: {dog[0]}, Occurrences: {dog[1]} ||" for dog in
                                most_common_dog_names_overall]
    names_and_occurs_males = [f"|| - Name: {dog[0]}, Occurrences: {dog[1]} ||" for dog in most_common_male_dog_names]
    names_and_occurs_female = [f"|| - Name: {dog[0]}, Occurrences: {dog[1]} ||" for dog in
                               most_common_female_dog_names]

    most_common_names = {"most_common_overall": names_and_occurs_overall,
                         "most_common_male": names_and_occurs_males,
                         "most_common_female": names_and_occurs_female}

    return most_common_names


def build_most_common_names_msg(most_common_names):
    join_most_common_dog_names = "\n".join(most_common_names["most_common_overall"])
    join_most_common_male_dog_names = "\n".join(most_common_names["most_common_male"])
    join_most_common_female_dog_names = "\n".join(most_common_names["most_common_female"])

    longest_output_overall = max(
        [len(name_and_occ) for name_and_occ in most_common_names["most_common_overall"]])
    longest_output_males = max([len(name_and_occ) for name_and_occ in most_common_names["most_common_male"]])
    longest_output_females = max(
        [len(name_and_occ) for name_and_occ in most_common_names["most_common_female"]])

    header_most_common_names_overall = print_header(longest_output_overall,
                                                    "TOP 10 MOST COMMON OVERALL DOG NAMES")
    header_most_common_male_dog_names = print_header(longest_output_males,
                                                     "TOP 10 MOST COMMON MALE DOG NAMES")
    header_most_common_female_dog_names = print_header(longest_output_females,
                                                       "TOP 10 MOST COMMON FEMALE DOG NAMES")

    footer_overall = print_footer(longest_output_overall)
    footer_male = print_footer(longest_output_males)
    footer_female = print_footer(longest_output_females)

    return f"\n{header_most_common_names_overall}" \
           f"\n{join_most_common_dog_names}\n" \
           f"{footer_overall}\n" \
           f"\n{header_most_common_male_dog_names}" \
           f"\n{join_most_common_male_dog_names}\n" \
           f"{footer_male}\n" \
           f"\n{header_most_common_female_dog_names}" \
           f"\n{join_most_common_female_dog_names}\n" \
           f"{footer_female}\n"


def dog_names_by_length(dog_names, length):
    return "\n".join(set([f"|| - {dog_name} ||" for dog_name in dog_names if len(dog_name) == length]))


def check_arguments(parser):
    if len(sys.argv) == 1 and "wuff.py" in sys.argv[0]:
        parser.print_help()
        sys.exit()

    elif not any(item.lower() in sys.argv for item in constants.parser_functions):
        if "-h" in sys.argv or "--h" in sys.argv:
            parser.print_help()
            sys.exit()

        else:
            sys.exit(constants.missing_function_parameter)

    for arg in sys.argv:
        if "-h" in sys.argv or "--h" in sys.argv:
            parser.print_help()
            sys.exit()

        elif arg.lower().startswith("-") and arg not in constants.parser_options or arg.lower().startswith(
                "--") and arg not in constants.parser_options:
            try:
                int(arg)
            except ValueError:
                sys.exit(constants.unexpected_arg)
