#!/usr/bin/env python3
import csv
import os
from sys import argv



def clean_int_str(int_str):
    int_str = int_str.replace("Under","0").replace("over","inf")
    return int_str.replace("$","").replace(",","")


def process_line_dict(line_dict):
    bracket_list = line_dict["Income bracket"].strip().split()
    bracket_min = clean_int_str(bracket_list[0])
    bracket_max = clean_int_str(bracket_list[-1])
    num = clean_int_str(line_dict["Number (1000s)"])
    mean = clean_int_str(line_dict["Mean (1000s)"])
    stderr = clean_int_str(line_dict["Standard Error"])
    return {
        "bracket_min": bracket_min,
        "bracket_max": bracket_max,
        "number": num,
        "mean": mean,
        "stderr": stderr,
    }



raw_filename = argv[1]
filename,ext = os.path.splitext(raw_filename)
out_filename = filename.replace("raw", "clean") + ext


with open(raw_filename, "rt") as raw_file, open(out_filename, "wt") as out_file:
    reader = csv.DictReader(raw_file, dialect="excel")
    writer = csv.DictWriter(out_file,
        ["bracket_min", "bracket_max", "number", "mean", "stderr"])
    writer.writeheader()
    for line in reader:
        new_line = process_line_dict(line)
        writer.writerow(new_line)

