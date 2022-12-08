import argparse
from wuff_stats import wuff_stats
from wuff_find import find_dog


def run(args):
    if args.function.lower() == "find":
        find_dog(args.name, args.year)
    elif args.function.lower() == "stats":
        wuff_stats()
    elif args.function.lower() == "create":
        print("CREATE")


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("function", help="available functions: find, stats, create")
    parser.add_argument("name", help="add a name for the find function")
    parser.add_argument("-y", "--year", default="", help="select a year")

    return parser


# change to args=None for prod
def main(args):
    parsed = get_parser().parse_args(args)
    run(parsed)


if __name__ == '__main__':
    # change to main() when in production
    main(["stats", "luna"])
