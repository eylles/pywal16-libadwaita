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
      with the corresponding rgb hex string
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
parser.add_argument(
    "-t",
    "--target",
    dest="targ",
    help="should be the PARENT dir "
    "containing the 'gtk-3.0' and 'gtk-4.0' dirs "
    "otherwise the target will default to: "
    "$XDG_CONFIG_HOME",
)


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
# substituting links and removing the rgba part is not needed here
# for keys, values in data["variables"].items():
#     data_sub_link(data["variables"], keys, values)
# for keys, values in data["variables"].items():
#     data_rgb_to_hex(data["variables"], keys, values)
if "sidebar_bg_color" not in data["variables"]:
    print("sidebar colors are not present, assigning them...")
    data["variables"].update(
            {"sidebar_bg_color": data["variables"]["window_bg_color"]}
            )
    data["variables"].update(
            {"sidebar_fg_color": data["variables"]["window_fg_color"]}
            )
    data["variables"].update(
            {"sidebar_backdrop_color": data["variables"]["view_bg_color"]}
            )
    data["variables"].update(
            {"sidebar_shade_color": data["variables"]["headerbar_shade_color"]}
            )


if args.debug:
    print("Corrected Data:")
    print("Name:", data["name"])
    # print("Vars:", data["variables"])
    for keys, values in data["variables"].items():
        print("{key: >24}: {value}".format(key=keys, value=values))

# construct output string to spit to css
css_s: str = ""

vars: str = ""
for k, v in data["variables"].items():
    vars = vars + "@define-color {} {};\n".format(k, v)

pal: str = ""
for tint, _ in data["palette"].items():
    for ind, col in data["palette"][tint].items():
        pal = pal + "@define-color {}{} {};\n".format(tint, ind, col)

css_s = vars + pal

# print(css_s)

gtk3: str = css_s
gtk4: str = css_s

if "custom_css" in data:
    gtk3 = gtk3 + "\n" + data["custom_css"]["gtk3"]
    gtk4 = gtk4 + "\n" + data["custom_css"]["gtk4"]

if args.debug:
    print("gtk3 stylesheet:")
    print(gtk3)
    print("")
    print("gtk4 stylesheet:")
    print(gtk4)
    print("")

if args.targ:
    target_dir = "{}".format(args.targ)
else:
    username = os.environ["USER"]
    home_dir = os.environ.get("HOME", "/home/{}".format(username))
    xdg_conf = os.environ.get("XDG_CONFIG_HOME", "{}/.config".format(home_dir))
    target_dir = "{}".format(xdg_conf)
    # print(target_dir)

target_gtk3 = "{}/gtk-3.0".format(target_dir)
# print(target_gtk3)
target_gtk4 = "{}/gtk-4.0".format(target_dir)
# print(target_gtk4)


def write_css(output_dir, output_string):
    if os.path.exists(output_dir):
        if args.debug:
            print("dir {} exists".format(output_dir))
    else:
        if args.debug:
            print("dir {} does not exist, creating it".format(output_dir))
        os.mkdir(output_dir)
    out_file = "{}/gtk.css".format(output_dir)
    with open(out_file, "w") as of:
        of.write(output_string)


write_css(target_gtk3, gtk3)
write_css(target_gtk4, gtk4)
