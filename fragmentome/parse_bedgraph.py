import argparse
import os
from subprocess import run

parser = argparse.ArgumentParser(description='Bedgraph editing')
parser.add_argument('file',
                    type=str,
                    help='input file')

args=parser.parse_args()
file = args.file
files = file.split(',')

out = open('edited.bedgraph', 'w')

if len(files) == 1:
    bedgraph = open(file, 'r')
    for line in bedgraph:
        out.write('chr' + line)

else:
    for i in files:
        bedgraph = open(i, 'r')
        for line in bedgraph:
            out.write('chr' + line)

out.close()
bedgraph.close()
print('DONE')

# command example
# python3.5 parse_bedgraph.py bedgraph.bedgraph,edit_bedgraph.bedgraph
