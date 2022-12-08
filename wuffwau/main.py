import argparse
import pathlib

from wuff_stats import wuff_stats
from wuff_find import find_dog
from wuff_create import wuff_create


def run(args):
    if args.function.lower() == "find":
        find_dog(args.name, args.year)
    elif args.function.lower() == "stats":
        wuff_stats()
    elif args.function.lower() == "create":
        wuff_create(args.output_dir)


def get_parser():
    current_dir = pathlib.Path.cwd()
    parser = argparse.ArgumentParser()
    parser.add_argument("function", help="available functions: find, stats, create")
    parser.add_argument("name", help="add a name for the find function")
    parser.add_argument("-y", "--year", default="", help="select a year")
    parser.add_argument("-o,", "--output-dir", default=current_dir,
                        help="specify a directory where the file with the created dog should be put")
    return parser


# change to args=None for prod
def main(args):
    parsed = get_parser().parse_args(args)
    run(parsed)


if __name__ == '__main__':
    # change to main() when in production
    main(["create", "luna"])
