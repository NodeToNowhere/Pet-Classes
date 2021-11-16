from classes.pet import Pet


class Customer:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.pets = []

    def reduce_cash(self, cash):
        self.cash -= cash

    def pet_count(self):
        return len(self.pets)

    def add_pet(self, pet):
        self.pets.append(pet)
