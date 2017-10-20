#!/usr/bin/python

"""
Takes a string with python format interpolation syntax and munges
in values from a csv file to be ran directly or output.

The following takes row 1 and 3 from the csv file and interpolates the string
and executes them.

If the csv has
hostname,dnsserver
mozilla.com,4.2.2.2

csv_interpolate.py -x -s -f "input.csv" -c "host {} {}" -d "1,3"
The preceeding would execute:

host mozilla.com 4.2.2.2
"""

import argparse
import csv
import subprocess
import sys


def interpolate(line, args):
    try:
        i_str = line.format(*args)
    except (IndexError, ValueError):
        print "Incorrect number of args for interpolation"
        sys.exit(2)
    return i_str


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-c', action="store", dest="cmd")
    parser.add_argument('-f', action="store", dest="csv")
    parser.add_argument('-s', action="store_true", dest="skip_header")
    parser.add_argument('-x', action="store_true", dest="execute")
    parser.add_argument('-d', action="store", dest="fields")

    args = parser.parse_args()
    if not args.cmd:
        print "cmd required"
        sys.exit(2)
    if not args.csv:
        print "csv required"
        sys.exit(2)
    if not args.fields:
        print "fields required"
        sys.exit(2)
    counter = 0
    with open(args.csv, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            if counter == 0 and args.skip_header:
                counter += 1
                continue
            tmp = []
            for i in args.fields.split(','):
                i = int(i)
                tmp.append(row[i])
            cmd = interpolate(args.cmd, tmp)
            if not args.execute:
                print cmd
            else:
                cmd_list = cmd.split()
                p = subprocess.Popen(
                    cmd_list,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                output, errors = p.communicate()
                print output
