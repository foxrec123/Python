
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.list_of_acquaintances = []
        print('{} is created'.format(self.name))

    def know(self, another_person):
        if not another_person in self.list_of_acquaintances:
            self.list_of_acquaintances.append(another_person)
            another_person.list_of_acquaintances.append(self)
            print('{} and {} are known now'.format(self.name, another_person.name))
        else:
            print('{} and {} have already known'.format(self.name, another_person.name))

    def is_known(self, another_person):
        if another_person in self.list_of_acquaintances:
            print('{} and {} are known'.format(self.name, another_person.name))
        else:
            print('{} and {} are not known'.format(self.name, another_person.name))


person_1 = Person('Victor', 28)
person_2 = Person('Alex', 20)
person_3 = Person('Jessica', 25)

print('\n')

person_1.know(person_3)
person_1.know(person_3)

print('\n')

person_1.is_known(person_2)
person_1.is_known(person_3)
person_3.is_known(person_1)
