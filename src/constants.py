import pathlib

from functions import print_header, print_footer

current_dir = pathlib.Path.cwd()

request_error = "Oops... an Error occurred while trying to get the dog data. " \
                "Check your network connection and try again."

req_err_header = print_header(len(request_error), "ERROR")
req_err_footer = print_footer(len(request_error))

invalid_output_dir_usage = 'The [-o | --output-dir] OUTPUT_DIR option ' \
                           'is only available for the create function!\n' \
                           'for additional information run main.py -h'

invalid_name_usage = 'The [-n | --name] NAME option is only available for the create function!\n' \
                     'for additional information run main.py -h'

missing_name_option = 'Please provide a name [-n | --name] NAME for the find function!\n' \
                      'for additional information run main.py -h'
