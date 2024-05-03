class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} added to the zoo!")
        else:
            print(f"{new_animal} already exists in the zoo.")

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")

    def sort_animals(self):
        sorted_animals = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter in sorted_animals:
                sorted_animals[first_letter].append(animal)
            else:
                sorted_animals[first_letter] = [animal]
        
        for key in sorted(sorted_animals.keys()):
            print(f"{key}: {sorted_animals[key]}")

    def get_groups(self):
        print("Animal groups:")
        self.sort_animals()

ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Giraffe") 

ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Lion")

ramat_gan_safari.get_groups()
