#!/usr/bin/python3.5

import argparse
parser = argparse.ArgumentParser(description='Extracting coordinates of fragment of certain size from SAM file to BED')
parser.add_argument('file',
                    type=str,
                    help='name  of file in sam format')
parser.add_argument('min_len',
                    type=int,
                    help='Minimum length of the fragment')
parser.add_argument('max_len',
                    type=int,
                    help='Maximum length of the fragment')

args=parser.parse_args()
file = args.file


down, up = args.min_len, args.max_len

bed_file = open(file+'.bed', 'w')
bed_file.write('name' + '\t' + 'chromosome' + '\t' + 'start_pos' + '\t' + 'stop_pos' + '\t' + 'fragment_length' + '\n')
sam = open(file, 'r')
for read in sam:
    if read.startswith('SRR'):
        read = read.split('\t')
        if int(read[8]) >= int(down) and int(read[8]) <= int(up)+1:
            stop_pos = int(read[7]) + 38
            bed_line = read[0] + '\t' + read[2] + '\t' + read[3] + '\t' + str(stop_pos) + '\t' + read[8] + '\t' + '\n'
            bed_file.write(bed_line)

bed_file.close()
print('Your BED is ready!')

# 8 - length
# 0 - name
# 3 - start coordinate
# 7 - coordinate of friend
# 2 - chromosome