"""
Everything Acme sells is considered a `Product`, and must have the
following fields (variables that live "inside" the class)
"""
from random import randint


class Product:
    def __init__(self, name):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        """
        if the ratio is less than 0.5 return "Not so stealable...",
        if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable.",
        and otherwise return "Very stealable!"
        """
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio >= 0.5 and ratio < 1:
            return "Kinda stealable"
        else:
            return "Very stealable!"

    def explode(self):
        """
        calculates the flammability times the weight, and then
          returns a message: if the product is less than 10 return "...fizzle.", if it is
          greater or equal to 10 but less than 50 return "...boom!", and otherwise
          return "...BABOOM!!"
        """
        explode = self.flammability * self.weight
        if explode < 10:
            return "...fizzle"
        elif explode >= 10 and explode < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """
    subclass of Product
    Change the default `weight` to 10 (but leave other defaults unchanged)
    - Override the `explode` method to always return "...it's a glove."
    - Add a `punch` method that returns "That tickles." if the weight is below 5,
      "Hey that hurt!" if the weight is greater or equal to 5 but less than 15, and
      "OUCH!" otherwise
    """

    def __init__(self, name):
        super().__init__(name)

        self.weight = 10

    def explode(self):
        """does not explode"""
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
