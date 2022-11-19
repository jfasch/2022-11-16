import sys

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        return self.firstname + ' ' + self.lastname

class Employee(Person):
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def title(self):
        return super().fullname() + ' (' + str(self.salary) + ')'

class Manager(Employee):
    def __init__(self, firstname, lastname, salary, employees):
        super().__init__(firstname, lastname, salary)
        self.employees = employees

    def title(self):
        return super().title() + ' (' + str(len(self.employees)) + ')'

    def add_employee(self, emp):
        if not isinstance(emp, Employee):
            print('geh weg!', file=sys.stderr)
            sys.exit(1)
        if emp is self:
            print('no!', file=sys.stderr)
            sys.exit(1)
        self.employees.append(emp)

joerg = Employee('Joerg', 'Faschingbauer', 10000)
caro = Employee('Caro', 'Faschingbauer', 500)
isi = Manager('Isolde', 'Haubentaucher', 100000, [joerg, caro])
philipp = Person('Philipp', 'Lichtenberger')

print(caro.title())
print(joerg.title())
print(isi.title())

print('ist caro ein Manager?', isinstance(caro, Manager))
print('ist isi ein Manager?', isinstance(isi, Manager))
i = 666
print('ist i ein Manager?', isinstance(i, Manager))

print('ist isi eine Person?', isinstance(isi, Person))

print('ist jeder Manager eine Person?', issubclass(Manager, Person))
print('ist jeder Manager ein Manager?', issubclass(Manager, Manager))

johanna = Employee('Johanna', 'Faschingbauer', 100)
isi.add_employee(johanna)

print(isi.title())

#isi.add_employee(isi)
#isi.add_employee(philipp)
#isi.add_employee(666)

print(isi.title())
