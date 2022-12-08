def year_handler(dog_data, dog_name, year):
    if len(year) > 0:
        return int(year)

    latest_year = max([int(row["StichtagDatJahr"]) for row in dog_data if
                       row["HundenameText"].lower() == dog_name.lower()])

    return latest_year


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
    return f"**{(output_length + 4) * '='}**"


def process_common_names(raw_names):
    names_and_occurrences = [f"|| - Name: {dog[0]}, Occurrences: {dog[1]} ||"
                             for dog in raw_names]

    longest_output = max([len(name_and_occ) for name_and_occ in names_and_occurrences])

    return {"names_and_occurrences": names_and_occurrences, "longest_output": longest_output}


def dog_names_by_length(dog_names, length):
    return "\n".join(
        set([f"|| - {dog_name} ||" for dog_name in dog_names if len(dog_name) == length]))
