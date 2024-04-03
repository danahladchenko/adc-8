class Dog:
    name = 'unknown'
    #class attibute
    def __init__(self, breed, age):
        self.is_walked = False
        self.breed = breed
        self.age = age
        self.tricks = []

    def walk(self):
        print('Dog walked')
        self.is_walked = True

    def learn_trick(self, trick):
        # if self.age >= 1 and trick == 'shake':
        #     self.tricks += [trick]  #selfl.trick.append(trick)
        # elif ...:
        #     ...
        # else:
        self.tricks += [trick]

    def do_trick(self):
        for trick in self.tricks:
            print(f'dog {self.name} of breed {self.breed} performs trick {trick}')
        if self.tricks == []:
            print(f'dog {self.name} of breed {self.breed} doesn\'t know any trick yet ')
        

class DogRex(Dog):
    name = 'Rex'

    # def sit(self):
    #     print(f'dog {self.name} is sitting ')

my_dog = DogRex('bulldog', 0)
print(f'my dog name is {my_dog.name}')
print(f'my dog age is{my_dog.age} years')
my_dog.learn_trick('sit')
my_dog.learn_trick('shake')
print(f'my dog tricks are is {my_dog.tricks}')