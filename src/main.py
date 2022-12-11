import argparse
import sys

from constants import current_dir, invalid_output_dir_usage, invalid_name_usage, missing_name_option
from wuff_create import wuff_create
from wuff_find import find_dog
from wuff_stats import wuff_stats
from functions import print_header, print_footer


def run(args):
    if args.function.lower() == "find":
        if not args.name:
            sys.exit(missing_name_option)

        find_dog(args.name, args.year)

    elif args.function.lower() == "stats":
        if args.output_dir != current_dir:
            sys.exit(invalid_output_dir_usage)
        if args.name:
            sys.exit(invalid_name_usage)

        wuff_stats(args.year)

    elif args.function.lower() == "create":
        if args.name:
            sys.exit(invalid_name_usage)

        wuff_create(args.output_dir, args.year)


def get_parser():
    parser_title = "Wuff and Wau"
    parser_description = "A command-line tool which offers various operations based on the open data of the " \
                         "registered dogs in the city of Zurich."
    parser_header = print_header(
        len(parser_description),
        parser_title)
    parser_footer = print_footer(len(parser_description))

    parser = argparse.ArgumentParser(description=f"{parser_header}\n|| - {parser_description} ||\n{parser_footer}",
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("function", help="available functions: find, stats, create\n"
                                         "----------------------------------------\n"
                                         "find:\n"
                                         "-----\n"
                                         "Search for dogs by a given name.\n"
                                         "required option(s): [-n | --name] NAME\n"
                                         "optional option(s): [-y | --year] YEAR\n"
                                         "---------------------------------------------------------------\n"
                                         "stats:\n"
                                         "------\n"
                                         "Show the following information about the dogs in Zurich:\n"
                                         "- Longest Dog Name(s)\n"
                                         "- Shortest Dog Name(s)\n"
                                         "- Top 10 most common Dog Names over all\n"
                                         "- Top 10 most common Male Dog Names\n"
                                         "- Top 10 most common Female Dog Names\n"
                                         "- Amount of Male Dog Names and Female Dog Names\n"
                                         "required option(s): NO REQUIRED OPTION(S)\n"
                                         "optional option(s): [-y | --year] YEAR\n"
                                         "---------------------------------------------------------------\n"
                                         "create:\n"
                                         "-------\n"
                                         "Creates a new dog with a random name, random birth year,\n"
                                         "random sex and a random dog media.\n"
                                         "The newly created dog will be saved to a specified directory.\n"
                                         "The name of the created dog file will be in the following format:\n"
                                         "dogname_birthyear.file-extension\n"
                                         "required option(s): NO REQUIRED OPTION(S)\n"
                                         "optional option(s): [-o | --output-dir] OUTPUT_DIR"
                        )

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-n", "--name", help="Add a name for the find function to search for dogs by the given name.")
    group.add_argument("-o,", "--output-dir", default=current_dir,
                       help="Specify a directory for the create function, "
                            "in which the file of the created dog should be saved.")

    parser.add_argument("-y", "--year", default="", help="Select a year for which the dog data should be filtered,\n"
                                                         "if no year is passed, the latest year "
                                                         "with available data will be chosen.")

    return parser


def main(args=None):
    parsed = get_parser().parse_args(args)
    run(parsed)


if __name__ == '__main__':
    main()
