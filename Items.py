from RaccoonPG import *
from NonRaccoon import *
from Combat import *

class Items():
    def __init__(self, name, item_type):
        self.name = name
        self.item_type = item_type

    def get_name(self):
        return self.name

    def get_item_type(self):
        return self.item_type

class Potion(Items):
    def __init__(self, name, item_type, value):
        super().__init__(name, item_type)
        self.value = value

    def drink(self, consumer):
        if (self.item_type == "Health"):
            consumer.increase_health(self.value)
        else:
            consumer.increase_mana(self.value)