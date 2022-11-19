import csv
from collections import namedtuple


# class Person:
#     def __init__(self, id, firstname, lastname, birth):
#         self.id = id
#         self.firstname = firstname
#         self.lastname = lastname
#         self.birth = birth

Person = namedtuple('Person', ('id', 'firstname', 'lastname', 'birth'))

def read_csv_header(filename):
    f = open(filename, encoding='cp1252')
    rdr = csv.DictReader(f, delimiter=';', quotechar='"')
    for record in rdr:
        yield Person(int(record['ID']), record['First name'], record['Last name'], record['Date of Birth'])

def read_csv_noheader(filename):
    f = open(filename, encoding='cp1252')
    rdr = csv.reader(f, delimiter=';', quotechar='"')
    for elem in rdr:    # ['1', 'Joerg;DI', 'Faschingbauer', '19.06.1966']
        yield Person(int(elem[0]), elem[1], elem[2], elem[3])

