import sys

filename = sys.argv[1]
f = open(filename)

for line in f:
    line = line.rstrip('\n')

    if line.lstrip().startswith('#'):
        continue
    if len(line.strip()) == 0:
        continue

    print(line)

    # if not (line.lstrip().startswith('#') or len(line.strip()) == 0):
    #     print(line)
