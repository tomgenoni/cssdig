import argparse
import sys

# Validate and format CSS first

my_list = sys.argv[1].split(",")

foo = ""

for s in my_list:
    foo += s

print foo
