# The Wuff and Wau CLI project

This command-line tool offers lookup operations on the open data of the registered dogs in the city of Zurich,
which can be found here: https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen_od1002

Additionally, it provides an option to create your own dog, with a random name, birth year, sex and media.
In the end the dog will be saved as a file to a provided directory
(if not provided, it will be saved in the current directory) in the following format:

dogname_birthyear.file-extension

## Using the CLI tool

1. Open up a terminal and navigate to the projects folder ```WuffWau```.
2. Run ```poetry shell``` to activate the virtual environment.
3. Run ```poetry install```to install the dependencies of the project.
4. Run the script with ```poetry run python src/wuff.py``` or navigate to the ```src```folder
   and run it with ```poetry run python wuff.py```, this will display more information
   about the CLI usage and an example.
5. The tool can also be run without poetry, you can just run it with

   ```python src/wuff.py```

   (keep in mind that you will still have to install the dependencies !)

### Additional information

The projects dependencies and packaging is managed with poetry (https://python-poetry.org)

The minimum required version of python to run the script is python 3.10 (defined in pyproject.toml)
