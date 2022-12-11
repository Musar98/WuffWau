import pathlib

from functions import print_header, print_footer

current_dir = pathlib.Path.cwd()

request_error = "Oops... an Error occurred while trying to make a network request. " \
                "Please check your network connection and try again."

req_err_header = print_header(len(request_error), "ERROR")
req_err_footer = print_footer(len(request_error))

parser_title = "Wuff and Wau"
parser_description = "A command-line tool which offers various operations based on the open data of the " \
                     "registered dogs in the city of Zurich."
parser_header = print_header(
    len(parser_description),
    parser_title)
parser_footer = print_footer(len(parser_description))

invalid_output_dir_usage = 'The [-o | --output-dir] OUTPUT_DIR option ' \
                           'is only available for the create function!\n' \
                           'for additional information run main.py -h'

invalid_name_usage = 'The [-n | --name] NAME option is only available for the create function!\n' \
                     'for additional information run main.py -h'

missing_name_option = 'Please provide a name [-n | --name] NAME for the find function!\n' \
                      'for additional information run main.py -h'

function_help_message = "available functions: find, stats, create\n" \
                        "----------------------------------------\n" \
                        "find:\n" \
                        "-----\n" \
                        "Search for dogs by a given name.\n" \
                        "required option(s): [-n | --name] NAME\n" \
                        "optional option(s): [-y | --year] YEAR\n" \
                        "---------------------------------------------------------------\n" \
                        "stats:\n" \
                        "------\n" \
                        "Show the following information about the dogs in Zurich:\n" \
                        "- Longest Dog Name(s)\n" \
                        "- Shortest Dog Name(s)\n" \
                        "- Top 10 most common Dog Names over all\n" \
                        "- Top 10 most common Male Dog Names\n" \
                        "- Top 10 most common Female Dog Names\n" \
                        "- Amount of Male Dog Names and Female Dog Names\n" \
                        "required option(s): NO REQUIRED OPTION(S)\n" \
                        "optional option(s): [-y | --year] YEAR\n" \
                        "---------------------------------------------------------------\n" \
                        "create:\n" \
                        "-------\n" \
                        "Creates a new dog with a random name, random birth year,\n" \
                        "random sex and a random dog media.\n" \
                        "The newly created dog will be saved to a specified directory.\n" \
                        "The name of the created dog file will be in the following format:\n" \
                        "dogname_birthyear.file-extension\n" \
                        "required option(s): NO REQUIRED OPTION(S)\n" \
                        "optional option(s): [-o | --output-dir] OUTPUT_DIR"

name_help_message = "Add a name for the find function to search for dogs by the given name."

output_dir_help_message = "Specify a directory for the create function, " \
                          "in which the file of the created dog should be saved."

year_help_message = "Select a year for which the dog data should be filtered,\n" \
                    "if no year is passed, the latest year " \
                    "with available data will be chosen."
