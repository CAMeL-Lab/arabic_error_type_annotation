import sys
from getopt import getopt
from scripts.alignment.al_align_annotate import process_align_annot_eval


def print_usage():
    print("Usage: annotate_eval_ar.py [OPTIONS] source target")
    print("where")
    print("  source          -   the source input")
    print("  target          -   the target side of a parallel corpus or a system output")
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
# process_align_annot_eval(ref_path, sys_path, False)
# print(ref_path, sys_path)

# ref_path = "sample/sample.m2"
# sys_path = "sample/sample_sys"
print("")


process_align_annot_eval(ref_path, sys_path, False)
