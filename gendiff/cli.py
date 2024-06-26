import argparse
import json


def open_filer(path):
    if path.endswith('.json'):
        with open(path) as f:
            file = json.load(f)
    return file



def parser_args():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file