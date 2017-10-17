class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')


my_dog = Dog('Jessie', 5)
fathers_dog = Dog('Bella', 10)

my_dog.sit()
my_dog.roll_over()
fathers_dog.sit()

print(fathers_dog.name.title() + ' is ' + str(fathers_dog.age) + ' years old')
