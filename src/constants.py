import pathlib

from functions import print_msg_builder

current_dir = pathlib.Path.cwd()

request_error_body = "Oops... an Error occurred while trying to make a network request. " \
                     "Please check your network connection and try again."

request_error = print_msg_builder("NETWORK REQUEST ERROR", request_error_body)

parser_description_title = "Wuff and Wau"
parser_description_body = "This command-line tool offers various lookup operations on the open data of the " \
                          "registered dogs in the city of Zurich."

parser_usage = "usage: wuff.py 'function' '-option' 'option value' ||\n" \
               "|| - example: wuff.py find(=function) -n(=option) Luna(=option value) ||\n" \
               "|| - options can be chained: wuff.py find -n Luna -y 2020 ||\n" \
               "|| - add the [-h | --help] flag to display the help message"

parser_description = print_msg_builder(parser_description_title, parser_description_body, parser_usage)

parser_add_info_msg = "for additional information run wuff.py -h"

invalid_output_dir_usage = 'The [-o | --output-dir] OUTPUT_DIR option is only available for the create function!'
invalid_name_usage = 'The [-n | --name] NAME option is only available for the create function!'
missing_name_option = 'Please provide a name [-n | --name] NAME for the find function!'

invalid_output_dir_msg = print_msg_builder(invalid_output_dir_usage, parser_add_info_msg)
invalid_name_usage_msg = print_msg_builder(invalid_name_usage, parser_add_info_msg)
missing_name_option_msg = print_msg_builder(missing_name_option, parser_add_info_msg)

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
