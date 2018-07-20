class Animal:
    def __init__(self, name, predator=False, poisonous=False):
        self.predator = predator
        self.poisonous = poisonous
        self.name = name

class Human:
    def is_dangerous(self, animal):
        if animal.poisonous or animal.predator:
            print('{} is dangerous'.format(animal.name))
        else:
            print('{} is not dangerous'.format(animal.name))

victor = Human()

snake = Animal(name='snake' ,poisonous=True)
bear = Animal(name='bear', predator=True)
cat = Animal('cat')

victor.is_dangerous(snake)
victor.is_dangerous(bear)
victor.is_dangerous(cat)


