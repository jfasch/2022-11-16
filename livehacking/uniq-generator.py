def uniq(seq):
    have = set()
    for num in seq:
        if num not in have:
            yield num
            have.add(num)



import sys

input_list = map(int, sys.argv[1:])
output_list = uniq(input_list)
for elem in output_list:
    print(elem)
