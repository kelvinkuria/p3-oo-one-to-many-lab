class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The object is not of type Pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)

if __name__ == "__main__":
    # Testing the classes
    owner1 = Owner("Alice")
    owner2 = Owner("Bob")

    pet1 = Pet("Buddy", "dog", owner1)
    pet2 = Pet("Whiskers", "cat", owner1)
    pet3 = Pet("Fluffy", "bird")

    owner1.add_pet(pet3)
    print(owner1.pets())  # [pet1, pet2, pet3]
    print(owner1.get_sorted_pets())  # [pet2, pet1, pet3]


