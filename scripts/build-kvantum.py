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

search_kvconfig = {
        "base": "#2e2e2e",
        "text_focus": "white",
        "button": "#4d4d4d",
        "light": "#535353",
        "mid_light": "#474747",
        "dark": "#282828",
        "mid": "#323232",
        "highlight": "#696969",
        "tooltip_text": "#efefef",
        "highlight_text": "#ffffff",
        "link": "#0057AE",
        "visited": "#E040FB",
        "text_normal": "#dfdfdf",
        "text_title": "#787878",
}

replace_kvconfig = {
        "base": data["variables"]["window_bg_color"],
        "text_focus": data["variables"]["window_fg_color"],
        "button": data["variables"]["shade_color"],
        "light": data["variables"]["window_bg_color"],
        "mid_light": data["variables"]["view_bg_color"],
        "dark": data["variables"]["view_bg_color"],
        "mid": data["variables"]["shade_color"],
        "highlight": data["variables"]["accent_bg_color"],
        "tooltip_text": data["variables"]["window_fg_color"],
        "highlight_text": data["variables"]["view_fg_color"],
        "link": data["variables"]["accent_color"],
        "visited": data["variables"]["accent_fg_color"],
        "text_normal": data["variables"]["window_fg_color"],
        "text_title": data["variables"]["view_fg_color"],
}

search_svg = {
        1: "#000000",
        2: "#090000",
        3: "#1e1e1e",
        4: "#212121",
        5: "#242424",
        6: "#2c2c2c",
        7: "#303030",
        8: "#31363b",
        9: "#3584e4",
        10: "#3d3d3d",
        11: "#3daee9",
        12: "#404040",
        13: "#414141",
        14: "#4285f4",
        15: "#444444",
        16: "#4990e7",
        17: "#4b4b4b",
        18: "#4f4f4f",
        19: "#525252",  # page color
        20: "#587392",
        21: "#5a5a5a",
        22: "#5a616e",
        23: "#616161",
        24: "#646464",
        25: "#666666",  # page color
        26: "#6e6e6e",
        27: "#707070",
        28: "#797979",
        29: "#93cee9",
        30: "#989898",
        31: "#acb1bc",
        32: "#b6b6b6",
        33: "#b74aff",
        34: "#c1c1c1",
        35: "#dfdfdf",
        36: "#eff0f1",
        37: "#f04a50",
        38: "#f2ffff",
        39: "#fcfcfc",
        40: "#ffffff",
}

replace_svg = {
        1: "#000000",
        2: "#090000",
        3: "#1e1e1e",
        4: "#212121",
        5: "#242424",
        6: "#2c2c2c",
        7: "#303030",
        8: data["variables"]["window_fg_color"],
        9: "#3584e4",
        10: "#3d3d3d",
        11: data["variables"]["accent_fg_color"],
        12: "#404040",
        13: "#414141",
        14: "#4285f4",
        15: "#444444",
        16: "#4990e7",
        17: "#4b4b4b",
        18: "#4f4f4f",
        19: "#525252",  # page color
        20: "#587392",
        21: "#5a5a5a",
        22: "#5a616e",
        23: "#616161",
        24: "#646464",
        25: "#666666",  # page color
        26: data["variables"]["accent_color"],
        27: "#707070",
        28: "#797979",
        29: data["variables"]["accent_fg_color"],
        30: "#989898",
        31: "#acb1bc",
        32: "#b6b6b6",
        33: "#b74aff",
        34: "#c1c1c1",
        35: "#dfdfdf",
        36: data["variables"]["window_bg_color"],
        37: "#f04a50",
        38: "#f2ffff",
        39: data["variables"]["view_bg_color"],
        40: "#ffffff",
}
