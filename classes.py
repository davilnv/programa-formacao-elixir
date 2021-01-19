import math


class Item():
    def __init__(self, name, quantity, price_item, price_weight, price_package):
        self.name = name
        self.quantity = quantity
        self.price_item = price_item
        self.price_weight = price_weight
        self.price_package = price_package

    def total_price(self):
        return (self.quantity * self.price_item)


class Person():
    def __init__(self, email):
        self.email = email

    def __str__(self):
        return self.email


class Cart():
    def __init__(self, list_items, list_people):
        self.list_items = list_items
        self.list_people = list_people
        self.total_price = 0

    def calculate_total(self):
        for item in self.list_items:
            self.total_price += item.total_price()

    def calculate_price_by_person(self):
        return (self.total_price / len(self.list_people))

    def return_price_by_person(self):
        result = dict()
        if(self.list_people is not None):
            for person in self.list_people:
                result[person.email] = round(
                    self.calculate_price_by_person()/100, 2)
            if(len(str(round(
                    self.calculate_price_by_person()/100, 2)).split('.')[1]) > 1):
                result[person.email] += 0.01
        return result
