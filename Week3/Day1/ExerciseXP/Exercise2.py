class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

davids_dog = Dog("Rex", 50)
print(f"David's dog details: Name - {davids_dog.name}, Height - {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog details: Name - {sarahs_dog.name}, Height - {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger.")
else:
    print("Both dogs are of the same height.")
