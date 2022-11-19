def uniq(seq):
    'uniquifies seq blah'
    uniquified = []
    have = set()
    for num in seq:
        if num not in have:
            uniquified.append(num)
            have.add(num)
    return uniquified



import sys

input_list = map(int, sys.argv[1:])
output_list = uniq(input_list)
for elem in output_list:
    print(elem)
