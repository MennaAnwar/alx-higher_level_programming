#!/usr/bin/python3
"""loads adds saves json to file"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
    __import__('6-load_from_json_file').load_from_json_file

try:
    jsonList = load_from_json_file("add_item.json")
except:
    jsonList = []

jsonList.extend(sys.argv[1:])
save_to_json_file(jsonList, "add_item.json")
