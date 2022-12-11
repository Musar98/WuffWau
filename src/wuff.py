import argparse
import sys

import constants
from wuff_create import wuff_create
from wuff_find import find_dog
from wuff_stats import wuff_stats


def run(args):
    if args.function.lower() == "find":
        if args.output_dir:
            sys.exit(constants.invalid_output_dir_usage)

        if not args.name:
            sys.exit(constants.missing_name_option)

        find_dog(args.name, args.year)

    elif args.function.lower() == "stats":
        if args.output_dir:
            sys.exit(constants.invalid_output_dir_usage)
        if args.name:
            sys.exit(constants.invalid_name_usage)

        wuff_stats(args.year)

    elif args.function.lower() == "create":
        if args.name:
            sys.exit(constants.invalid_name_usage)

        wuff_create(args.output_dir, args.year)


def get_parser():
    parser = argparse.ArgumentParser(description=f"{constants.parser_header}\n"
                                                 f"|| - {constants.parser_description} ||\n"
                                                 f"{constants.parser_footer}",
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("function", help=constants.function_help_message)

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-n", "--name", help=constants.name_help_message)
    group.add_argument("-o,", "--output-dir", help=constants.output_dir_help_message)

    parser.add_argument("-y", "--year", default="default", help=constants.year_help_message)

    return parser


def wuff(args=None):
    parsed = get_parser().parse_args(args)
    run(parsed)


if __name__ == '__main__':
    wuff()
