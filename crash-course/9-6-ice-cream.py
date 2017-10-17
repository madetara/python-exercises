class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + ' restaurant offers ' +
              self.cuisine_type)
        if self.cuisine_type != 'ice cream':
            print(' cuisine')

    def open_restaurant(self):
        print('The ' + self.restaurant_name + ' is open!')


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavors

    def display_flavors(self):
        print('Flavors: ' + ', '.join(self.flavours))


amorino = IceCreamStand('Amorino', 'ice cream', ['spumoni', 'strawberry',
                                                 'grape nut'])

amorino.describe_restaurant()
amorino.display_flavors()
