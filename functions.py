import argparse
import sys
import os
def parse_command():
    parser = argparse.ArgumentParser()
    parser.add_argument('strings', metavar='S', type=str, nargs='+')
    args = parser.parse_args()
    return args.strings


def run_command(command):
    if command[0] == '1':
        print(sys.version)
    elif command[0] == '2':
        filename = command[1]
        if not os.path.exists(filename):
            os.makedirs(filename)
    else:
        current_directory = os.getcwd()
        parent_directory = os.path.dirname(current_directory)
        items = os.listdir(parent_directory)
        for item in items:
            print(item)
