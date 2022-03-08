from sqlite3 import paramstyle
import sys
import codecs
from getopt import getopt
import argparse
from scripts.annotation.an_annote_sys_ref import annote_ref_sys

def print_usage():
    print("Usage: annotate_err_type_ar.py [OPTIONS] source target")
    print("where")
    print("  reference          -   the reference file")
    print("  target          -   the system's output")
    print("OPTIONS")

    print(
        "        --output  	                  -  The output file. "
        "Otherwise, it prints to standard output ")

parser = argparse.ArgumentParser()
parser.add_argument('--sys_path', type=str, required=True,
                    help="System's Output")

parser.add_argument('--ref_path', type=str, required=True,
                    help="Reference file")

parser.add_argument('--output_path', type=str,
                    help="Output file path")

parser.add_argument('--show_edit_paths', action="store_true",
                    help="Whether to show the orthographic and "
                    "morphological edits paths")

args = parser.parse_args()

lines = annote_ref_sys(args.ref_path, args.sys_path, args.show_edit_paths)

if args.output_path:
    write_output = codecs.open(args.output_path, 'w', "utf8")
    write_output.write(lines)
    write_output.close()
else:
    sys.stdout.write(lines)
