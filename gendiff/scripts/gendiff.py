#!/usr/bin/env python3

from gendiff import generate_diff
from gendiff.cli import parser_args


def main():
    first_file, second_file = parser_args()
    diff = generate_diff(first_file, second_file)
    print(diff)


if __name__ == '__main__':
    main()

