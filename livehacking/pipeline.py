import random

def random_generator(lo, hi):
    while True:
        yield random.randrange(lo, hi)

def uniq(seq):
    have = set()
    for num in seq:
        if num not in have:
            yield num
            have.add(num)

def squares(seq):
    for num in seq:
        yield num**2

        
for num in squares(uniq(random_generator(0, 100))):
    print(num)
