import sys
import codecs
from getopt import getopt
from scripts.annotation.an_annote_sys_ref import annote_ref_sys


def print_usage():
    print("Usage: annotate_err_type_ar.py [OPTIONS] source target")
    print("where")
    print("  reference          -   the reference file")
    print("  target          -   the system's output")
    print("OPTIONS")

    print(
        "        --output  	                  -  The output file. Otherwise, it prints to standard output ")


opts, args = getopt(sys.argv[1:], "v",
                    ["output="])

output = None

# print (opts)
for o, v in opts:
    if o == '--output':
        output = v
    else:
        print(sys.stderr, "Unknown option :", o)
        print_usage()
        sys.exit(-1)

# starting point
if len(args) != 2:
    print_usage()
    sys.exit(-1)

ref_path = args[1]
sys_path = args[0]

lines = annote_ref_sys(ref_path, sys_path)

if output:
    write_output = codecs.open(output, 'w', "utf8")
    write_output.write(lines)
    write_output.close()
else:
    sys.stdout.write(lines)
