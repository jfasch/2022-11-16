import time

def squares(seq):
    for num in seq:
        yield num**2

sqs = squares(range(10))
for num in sqs:
    print(num)
