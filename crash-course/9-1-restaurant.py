class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + ' restaurant offers ' +
              self.cuisine_type + ' cuisine')

    def open_restaurant(self):
        print('The ' + self.restaurant_name + ' is open!')


epicure = Restaurant('Epicure', 'french')
print(epicure.restaurant_name.title())
print(epicure.cuisine_type.title())

epicure.describe_restaurant()
epicure.open_restaurant()
print()

del_posto = Restaurant('Del posto', 'italian')
moments = Restaurant('Moments', 'spanish')

del_posto.describe_restaurant()
moments.describe_restaurant()
