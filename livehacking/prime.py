import sys

if len(sys.argv) == 1:
    number = input('Bitte gib die zu checkende Zahl ein: ')
else:
    number = sys.argv[1]

number = int(number)

if number == 1:
    print('not prime')
    sys.exit(0)

divisor_candidate = 2
while divisor_candidate < number:
    if number % divisor_candidate == 0:
        print('not prime')
        break
    divisor_candidate += 1
else:
    print('prime')
