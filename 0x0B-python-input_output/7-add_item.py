#!/usr/bin/python3
"""Load, add, save file function"""
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

file1 = "add_item.json"
try:
    list1 = load_from_json_file(file1)
except:
    list1 = []

for args in sys.argv[1:]:
    list1.append(args)

save_to_json_file(list1, file1)
