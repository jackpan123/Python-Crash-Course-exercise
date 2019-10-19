class Restaurant():
    """这是一家餐馆"""
    
    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_severd = 0

    def describe_restaurant(self):
        print("This restaurant name is " + self.restaurant_name.title()
        + " and type is " + self.restaurant_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open!")

    def set_number_served(self, number):
        if number >= self.number_severd:
            self.number_severd = number
        else:
            print("You can't roll back served number!")
        print("The served number is " + str(self.number_severd))

    def increment_number_served(self, increment_number):
        if increment_number > 0:
            self.number_severd += increment_number
        else:
            print("You can't increment passtive number!")

    def read_number_served(self):
        print("Served number is " + str(self.number_severd))

class IceCreamStand(Restaurant):
    """冰淇淋小店的简单尝试"""

    def __init__(self, restaurant_name, restaurant_type, flavors):
        super().__init__(restaurant_name, restaurant_type)
        self.flavors = flavors

    def show_flavors(self):
        for flavor in self.flavors:
            print("- " + flavor)

flavors = ['makalong', 'orange', 'apple']
cream_shop = IceCreamStand('jack', 'ice cream', flavors)
cream_shop.show_flavors()
