import sys
from getopt import getopt
from scripts.annotation.an_annote_sys_ref import annote_ref_sys


def print_usage():
    print("Usage: annotate_err_type_ar.py [OPTIONS] source target")
    print("where")
    print("  reference          -   the reference file")
    print("  target          -   the system's output")
    print("OPTIONS")
    # print("  -v    --verbose                   	-  print verbose output")
    # print("        --very_verbose              	-  print lots of verbose output")
    # print(
    #     "        --max_unchanged_words N     	-  Maximum unchanged words when extraction edit. Default 0.")
    # print(
    #     "        --ignore_whitespace_casing  	-  Ignore edits that only affect whitespace and caseing. Default no.")
    # print(
    #     "        --output  	                  -  The output file. Otherwise, it prints to standard output ")


opts, args = getopt(sys.argv[1:], "v",
                    ["max_unchanged_words=", "beta=", "verbose", "ignore_whitespace_casing", "very_verbose", "output="])

# starting point

if len(args) != 2:
    print_usage()
    sys.exit(-1)

ref_path = args[0]
sys_path = args[1]

annote_ref_sys(ref_path, sys_path)
