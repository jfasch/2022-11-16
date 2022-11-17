import sys
import primeness

if len(sys.argv) == 1:
    number = input('Bitte gib die zu checkende Zahl ein: ')
else:
    number = sys.argv[1]
number = int(number)

if primeness.is_prime(number):
    print('prime')
else:
    print('not prime')
