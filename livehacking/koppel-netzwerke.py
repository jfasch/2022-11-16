import csv
import sys

filename = sys.argv[1]

f = open(filename)
rdr = csv.reader(f)

for rowno, row in enumerate(rdr):
    if rowno == 0:
        continue
    freq, gain, phase = map(float, row)
    print(f'Freq: {freq}, Gain: {gain}, Phase: {phase}')
