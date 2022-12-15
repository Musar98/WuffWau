import pathlib

from functions import print_msg_builder

parser_functions = ["find", "stats", "create"]

current_dir = pathlib.Path.cwd()

request_error_body = "Oops... an Error occurred while trying to make a network request. " \
                     "Please check your network connection and try again."

request_error = print_msg_builder("NETWORK REQUEST ERROR", request_error_body)

parser_description_title = "Wuff and Wau"
parser_description_body = "This command-line tool offers a 'find' and 'stats' operation on the open data of the " \
                          "registered dogs in the city of Zurich."

parser_usage = "Additionally you can create your own dog, with a random name, birth year, sex and media.\n" \
               "|| - usage: wuff.py 'function' '-option' 'option value'||\n" \
               "|| - example: wuff.py find(=function) -n(=option) Luna(=option value) ||\n" \
               "|| - please keep in mind that the 'function' is required ! ||\n" \
               "|| - options can be chained: wuff.py find -n Luna -y 2020 ||\n" \
               "|| - add the [-h | --help] flag to any command to display this message and the info below"

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
                        'Search for dogs by a given name.\n' \
                        'If the name contains spaces e.g. Lord Nelson,\n' \
                        'you have to wrap the name in quotes: "Lord Nelson"\n' \
                        "\nReturns the dogs name, birth year and sex\n" \
                        "\nrequired option(s): [-n | --name] NAME\n" \
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
                        "\nrequired option(s): NO REQUIRED OPTION(S)\n" \
                        "optional option(s): [-y | --year] YEAR\n" \
                        "---------------------------------------------------------------\n" \
                        "create:\n" \
                        "-------\n" \
                        "Creates a new dog with a random name, random birth year,\n" \
                        "random sex and a random dog media.\n" \
                        "The newly created dog will be saved as a file to a specified directory.\n" \
                        "The name of the file will be in the following format:\n" \
                        "dogname_birthyear.file-extension\n" \
                        "\nrequired option(s): NO REQUIRED OPTION(S)\n" \
                        "optional option(s): [-o | --output-dir] OUTPUT_DIR\n" \
                        "                    [-y | --year] YEAR\n" \
                        "--------------------------------------------------------------------------"

name_help_message = 'Add a name for the find function to search for dogs by the given name.\n' \
                    'If the name contains spaces e.g. Lord Nelson, you have to wrap the name in quotes: "Lord Nelson"'

output_dir_help_message = "Specify a directory/path for the create function,\n" \
                          "in which the file of the created dog should be saved.\n" \
                          "If no path is provided, the file will be created in the current directory."

year_help_message = "Select a year for which the dog data should be filtered.\n" \
                    "If no year is provided, the latest year with available data will be taken."

missing_function_parameter = print_msg_builder("NO VALID FUNCTION PROVIDED", "The function argument is required !",
                                               "available functions: find,stats,create\n"
                                               "|| - For additional information,\n"
                                               "||   add the [-h | --help] flag\n"
                                               "||   to your previous command.")
