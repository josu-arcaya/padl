#!/usr/bin/env python3

import sys

from lint.utils import Padl

def validate_it(input_data):
    Padl(input_data).validate()
    return "Valid!"

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(validate_it(input_data))
    else:
        print('You need to provide a PADL file to be validated (i.e. python padl.py ./pipeline.yml)')

