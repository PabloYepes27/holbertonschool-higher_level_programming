#!/usr/bin/python3
"""[summary]"""


import os
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

if __name__ == '__main__':
    filename = "add_item.json"
    if os.path.isfile(filename):
        "evaluate if the file name exist"
        ls = load_from_json_file(filename)
        "loads the list file if it exist"
        ls += sys.argv[1:]
        "it concatenates the list with the new arguments"
        save_to_json_file(list(ls), filename)
        "it saves the arguments"
    else:
        "if the file doesn't exist, it creates it"
        save_to_json_file(sys.argv[1:], filename)
