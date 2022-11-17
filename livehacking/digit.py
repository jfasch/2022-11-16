import sys

translation_table = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

digit = int(sys.argv[1])
try:
    print(translation_table[digit])
except KeyError as e:
    print('bad input', file=sys.stderr)
    sys.exit(42)
