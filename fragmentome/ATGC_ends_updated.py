# This script counts nucleotide frequency at first 10 and last 10 positions

import collections
import os
counter = collections.Counter()
positions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2]

all_files = os.listdir()
files = []
for tmp_file in all_files:
    if tmp_file.endswith('seq'):
        files.append(tmp_file)

for file in files:
    if len(file) == 19:
        chr = file[-6:-4]
    else:
        chr = file[-5:-4]

    file_name = file[:-4] + '_freq_part.txt'
    print(file_name)
    out_table = open(file_name, 'w')
    out_table.write('position\tA\tT\tG\tC\tG+C\n')


    ex = open(file, 'r')
    for ind in positions:
        for frag in ex:
            counter[frag[ind]] += 1

        total_nucl = int(counter["A"]) + int(counter["C"]) + int(counter["G"]) + int(counter["T"])
        out_table.write(chr + '\t' + str(ind + 1) + '\t' + str(counter['A']/total_nucl)[:5] + '\t' + str(counter['T']/total_nucl)[:5] + '\t' +
                    str(counter['G']/total_nucl)[:5] + '\t' + str(counter['C']/total_nucl)[:5] + '\t' +
                    str(counter['G']/total_nucl + counter['C']/total_nucl)[:5] + '\n')

        counter.clear()
        ex.seek(0)

