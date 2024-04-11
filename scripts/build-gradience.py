#!/usr/bin/env python3

import json
import argparse
import sys
import os


#############
# functions #
#############


def hex_to_rgb(color):
    """Convert a hex color to rgb."""
    return tuple(bytes.fromhex(color.strip("#")))


def rgb_to_hex(color):
    """Convert an rgb color to hex."""
    return "#%02x%02x%02x" % (*color,)


def darken_color(color, amount):
    """Darken a hex color."""
    # color = [int(col * (1 - amount)) for col in hex_to_rgb(color)]
    ctup = hex_to_rgb(color)
    nctup = []
    for col in ctup:
        nctup.append(int(col * (1 - (amount/100))))
    return rgb_to_hex(nctup)


def lighten_color(color, amount):
    """Lighten a hex color."""
    # color = [int(col + (255 - col) * amount) for col in hex_to_rgb(color)]
    ctup = hex_to_rgb(color)
    nctup = []
    for col in ctup:
        nctup.append(int(col + (255 - col) * (amount/100)))
    return rgb_to_hex(nctup)


def blend_color(color, color2):
    """Blend two colors together."""
    r1, g1, b1 = hex_to_rgb(color)
    r2, g2, b2 = hex_to_rgb(color2)

    r3 = int(0.5 * r1 + 0.5 * r2)
    g3 = int(0.5 * g1 + 0.5 * g2)
    b3 = int(0.5 * b1 + 0.5 * b2)

    return rgb_to_hex((r3, g3, b3))


########
# Main #
########

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-d", "--debug", action='store_true',
                    help="Show Debug Output")
parser.add_argument("-n", "--dry-run", dest='dryrun', action='store_true',
                    help="do not write output files")
parser.add_argument("--pwfox", dest='pwfox', action='store_true',
                    help="pywalfox matching colors")

# Read arguments from command line
args = parser.parse_args()

if args.debug:
    print("Displaying Debug Output of % s" % parser.prog)

username = os.environ['USER']
base_cache_dir = os.environ.get('XDG_CACHE_HOME',
                                '/home/{}/.cache/'.format(username))
wal_cache_file = base_cache_dir + '/wal/colors.json'

with open(wal_cache_file) as json_file:
    data = json.load(json_file)
    if args.debug:
        print("Data read from file:", wal_cache_file)
        # print("Name:", data["name"])
        # print("Vars:", data["variables"])
        for keys, values in data["colors"].items():
            print("{key: >24}: {value}".format(key=keys, value=values))

col = {
    "col0": data["colors"]["color0"],
    "col1": data["colors"]["color1"],
    "col2": data["colors"]["color2"],
    "col3": data["colors"]["color3"],
    "col4": data["colors"]["color4"],
    "col5": data["colors"]["color5"],
    "col6": data["colors"]["color6"],
    "col7": data["colors"]["color7"],
    "col8": data["colors"]["color8"],
    "col9": data["colors"]["color9"],
    "col10": data["colors"]["color10"],
    "col11": data["colors"]["color11"],
    "col12": data["colors"]["color12"],
    "col13": data["colors"]["color13"],
    "col14": data["colors"]["color14"],
    "col15": data["colors"]["color15"],
}

if args.pwfox:
    pwf_l = 1.25
    pwf_e_l = 1.85
    pwf_e_e_l = 2.15

    bgt = hex_to_rgb(col["col0"])
    # print("bg hex: {h} rgb: {t}".format(h=col["col0"], t=bgt))
    # print(bgtuple[0])
    # print(bgtuple[1])
    # print(bgtuple[2])
    bg_l = []
    bg_l.append(min((max(0, int(bgt[0] + (bgt[0] * pwf_l)))), 255))
    bg_l.append(min((max(0, int(bgt[1] + (bgt[1] * pwf_l)))), 255))
    bg_l.append(min((max(0, int(bgt[2] + (bgt[2] * pwf_l)))), 255))
    bg_e_l = []
    bg_e_l.append(min((max(0, int(bgt[0] + (bgt[0] * pwf_e_l)))), 255))
    bg_e_l.append(min((max(0, int(bgt[1] + (bgt[1] * pwf_e_l)))), 255))
    bg_e_l.append(min((max(0, int(bgt[2] + (bgt[2] * pwf_e_l)))), 255))
    bg_e_e_l = []
    bg_e_e_l.append(min((max(0, int(bgt[0] + (bgt[0] * pwf_e_e_l)))), 255))
    bg_e_e_l.append(min((max(0, int(bgt[1] + (bgt[1] * pwf_e_e_l)))), 255))
    bg_e_e_l.append(min((max(0, int(bgt[2] + (bgt[2] * pwf_e_e_l)))), 255))
    bglight = rgb_to_hex(bg_l)
    bgexlight = rgb_to_hex(bg_e_l)
    bgeexlight = rgb_to_hex(bg_e_e_l)
    # print(bg_l)
    # print(bg_e_l)
    # print("bg l: {}".format(rgb_to_hex(bg_l)))
    # print("bg el: {}".format(rgb_to_hex(bg_e_l)))
    ec1 = bglight
    ec2 = bgexlight
    ec3 = bgeexlight
else:
    ec1 = lighten_color(col["col0"], 1)
    ec2 = lighten_color(col["col0"], 2)
    ec3 = lighten_color(col["col0"], 3)


col["cole1"] = ec1
col["cole2"] = ec2
col["cole3"] = ec3

gradience_theme = {
    "name": "pywal",
    "variables": {
        "accent_color": col["col12"],
        "accent_bg_color": col["col12"],
        "accent_fg_color": lighten_color(col["col12"], 70),
        "destructive_color": col["col11"],
        "destructive_bg_color": col["col3"],
        "destructive_fg_color": lighten_color(col["col11"], 70),
        "success_color": col["col13"],
        "success_bg_color": col["col13"],
        "success_fg_color": col["col15"],
        "warning_color": col["col14"],
        "warning_bg_color": col["col6"],
        "warning_fg_color": col["col15"],
        "error_color": col["col11"],
        "error_bg_color": col["col3"],
        "error_fg_color": col["col15"],
        "window_bg_color": col["col0"],
        "window_fg_color": col["col15"],
        "view_bg_color": col["cole1"],
        "view_fg_color": col["col15"],
        "headerbar_bg_color": col["col0"],
        "headerbar_fg_color": col["col15"],
        "headerbar_border_color": col["cole3"],
        "headerbar_backdrop_color": col["col4"],
        "headerbar_shade_color": col["cole2"],
        "card_bg_color": col["cole2"],
        "card_fg_color": col["col15"],
        "card_shade_color": col["cole1"],
        "dialog_bg_color": col["col0"],
        "dialog_fg_color": col["col15"],
        "popover_bg_color": col["col0"],
        "popover_fg_color": col["col15"],
        "shade_color": col["cole3"],
        "scrollbar_outline_color": col["col12"],
        "sidebar_bg_color": col["col0"],
        "sidebar_fg_color": col["col15"],
        "sidebar_backdrop_color": col["cole1"],
        "sidebar_shade_color": col["cole2"],
    },
    "palette": {
        "blue_": {
            "1": "#99c1f1",
            "2": "#62a0ea",
            "3": "#3584e4",
            "4": "#1c71d8",
            "5": "#1a5fb4"
        },
        "green_": {
            "1": "#8ff0a4",
            "2": "#57e389",
            "3": "#33d17a",
            "4": "#2ec27e",
            "5": "#26a269"
        },
        "yellow_": {
            "1": "#f9f06b",
            "2": "#f8e45c",
            "3": "#f6d32d",
            "4": "#f5c211",
            "5": "#e5a50a"
        },
        "orange_": {
            "1": "#ffbe6f",
            "2": "#ffa348",
            "3": "#ff7800",
            "4": "#e66100",
            "5": "#c64600"
        },
        "red_": {
            "1": "#f66151",
            "2": "#ed333b",
            "3": "#e01b24",
            "4": "#c01c28",
            "5": "#a51d2d"
        },
        "purple_": {
            "1": "#dc8add",
            "2": "#c061cb",
            "3": "#9141ac",
            "4": "#813d9c",
            "5": "#613583"
        },
        "brown_": {
            "1": "#cdab8f",
            "2": "#b5835a",
            "3": "#986a44",
            "4": "#865e3c",
            "5": "#63452c"
        },
        "light_": {
            "1": "#ffffff",
            "2": "#f6f5f4",
            "3": "#deddda",
            "4": "#c0bfbc",
            "5": "#9a9996"
        },
        "dark_": {
            "1": "#77767b",
            "2": "#5e5c64",
            "3": "#3d3846",
            "4": "#241f31",
            "5": "#000000"
        }
    },
    "custom_css": {
        "gtk4": "",
        "gtk3": ""
    },
    "plugins": {}
}

if args.debug:
    print("gradience theme values")
    for keys, values in gradience_theme["variables"].items():
        print("{key: >24}: {value}".format(key=keys, value=values))

home_dir = os.environ.get('HOME', '/home/{}'.format(username))
gr_dir = ".var/app/com.github.GradienceTeam.Gradience/config/presets/user"
out_dir = "{}/{}".format(home_dir, gr_dir)
theme_file = "pywal.json"
o_file = "{d}/{f}".format(d=out_dir, f=theme_file)

if not args.dryrun:
    if args.debug:
        print("writing {}".format(o_file))
    with open(o_file, "w") as outfile:
        json.dump(gradience_theme, outfile, indent=4)
else:
    if args.debug:
        print("dry run mode, no file written")
