#!/usr/bin/env python3

from growser.growser import print_shopping_list, parse_options
from growser.data import Data
from growser.pantry import from_file

from menu import all_dishes, menu
from extras import extras
from units import definitions as unit_defs

if __name__ == "__main__":
    options = parse_options()
    data = Data(
        menu=menu,
        all_dishes=all_dishes,
        extras=extras,
        pantry=from_file(options.pantry_file, unit_defs),
        units=unit_defs
    )
    print_shopping_list(options, data)