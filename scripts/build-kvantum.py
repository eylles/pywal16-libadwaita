#!/usr/bin/env python3

import json
import argparse
import sys
import os


#############
# functions #
#############

def data_sub_link(dictio, key, value):
    """
    return type: void
    description:
      replace the "@key_name" links
      with the color string value of
      the refferenced key
    """
    if value.find("@") > -1:
        index_str = value[1:]
        dictio[key] = dictio[index_str]
        if args.debug:
            print("{k}: {v}".format(k=key, v=dictio[key]))


def data_rgb_to_hex(dictio, key, value):
    """
    return type: void
    description:
      replace the "rgba()" values
      with the correspinding rgb hex string
    """
    if value.find("rgb") > -1:
        oparen = value.find("(")
        cparen = value.find(")")
        # index_str = value[1:]
        vallist = value[oparen+1:cparen].split(",")
        r = int(vallist[0])
        g = int(vallist[1])
        b = int(vallist[2])
        res = "#{0:02x}{1:02x}{2:02x}".format(r, g, b)
        dictio[key] = res
        if args.debug:
            print("{k}: {v}".format(
                k=key, v=dictio[key]))


########
# Main #
########

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-f", "--file", required="true", help="JSON file to use")
parser.add_argument("-d", "--debug", action='store_true',
                    help="Show Debug Output")

# Read arguments from command line
args = parser.parse_args()

if args.debug:
    print("Displaying Debug Output of % s" % parser.prog)
    print("File '{}' selected".format(args.file))

with open(args.file) as json_file:
    data = json.load(json_file)
    if args.debug:
        print("Data read from file:", args.file)
        print("Name:", data["name"])
        # print("Vars:", data["variables"])
        for keys, values in data["variables"].items():
            print("{key: >24}: {value}".format(key=keys, value=values))

# correct data
for keys, values in data["variables"].items():
    data_sub_link(data["variables"], keys, values)
for keys, values in data["variables"].items():
    data_rgb_to_hex(data["variables"], keys, values)


if args.debug:
    print("Corrected Data:")
    print("Name:", data["name"])
    # print("Vars:", data["variables"])
    for keys, values in data["variables"].items():
        print("{key: >24}: {value}".format(key=keys, value=values))
