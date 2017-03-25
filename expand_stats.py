#!/usr/bin/env python3
import csv
import os
from sys import argv

import numpy as np


def compute_bracket_flat(line_dict):
    lines = [int(line_dict["mean"])
        for i in range(int(line_dict["number"]))]
    return lines


def save_csv(in_filename, out_filename):
    with open(in_filename, "rt") as in_file, open(out_filename, "wt") as out_file:
        reader = csv.DictReader(in_file)
        writer = csv.DictWriter(out_file,["income"])
        writer.writeheader()
        for i,line in enumerate(reader):
            new_lines = compute_bracket_flat(line)
            new_lines = {"income":v for v in new_lines}
            print("bracket {}".format(i))
            for new_line in new_lines:
                writer.writerow(new_line)


def save_numpy(in_filename, out_filename):
    with open(in_filename, "rt") as in_file, open(out_filename, "wb") as out_file:
        reader = csv.DictReader(in_file)
        incomes = np.array([])
        for i,line in enumerate(reader):
            new_lines = np.array(compute_bracket_flat(line), dtype=np.uint32)
            print("bracket {}".format(i))
            incomes = np.concatenate([incomes, new_lines], axis=0)
        print("type of data: {incomes.dtype}")
        np.save(out_file, incomes)


if __name__ == "__main__":
    in_filename = argv[1]
    filename,ext = os.path.splitext(in_filename)

    # out_filename = filename.replace("clean", "expanded") + ext
    # save_csv(in_filename, out_filename)

    out_filename = filename.replace("clean", "expanded") + ".npy"
    save_numpy(in_filename, out_filename)


