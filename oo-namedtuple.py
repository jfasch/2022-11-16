from collections import namedtuple

Person = namedtuple('Person', ('id', 'firstname', 'lastname', 'birth'))

joerg = Person(1, 'Joerg', 'Faschingbauer', '19.06.1966')

print(joerg.id, joerg.firstname, joerg.lastname, joerg.birth)
