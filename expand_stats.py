#!/usr/bin/env python3
import csv
import os
from sys import argv

import numpy as np


def compute_bracket_flat(line_dict):
    lines = [{"income":line_dict["mean"]}
        for i in range(int(line_dict["number"]))]
    return lines

in_filename = argv[1]
filename,ext = os.path.splitext(in_filename)
out_filename = filename.replace("clean", "expanded") + ext


with open(in_filename, "rt") as in_file, open(out_filename, "wt") as out_file:
    reader = csv.DictReader(in_file)
    writer = csv.DictWriter(out_file,["income"])
    writer.writeheader()
    for i,line in enumerate(reader):
        new_lines = compute_bracket_flat(line)
        print("bracket {}".format(i))
        for new_line in new_lines:
            writer.writerow(new_line)

