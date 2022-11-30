import argparse
import csv
import requests as req


def get_data():
    response = req.get("https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen_od1002/download/KUL100OD1002.csv")
    decoded_response = response.content.decode("utf-8-sig")

    return decoded_response


def main(args=None):
    parsed = get_parser().parse_args(args)
    run(parsed)


def run(args):
    if args.function.lower() == "find":
        print("FIND")
    elif args.function.lower() == "stats":
        print("STATS")
    elif args.function.lower() == "create":
        print("CREATE")


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("function", help="available functions: find, stats, create")
    parser.add_argument("name", help="add a name for the find function")

    return parser


if __name__ == '__main__':
    main()
