favorite_fruits_str = input("Please enter your favorite fruit : ")

favorite_fruits = favorite_fruits_str.split()

chosen_fruit = input("Now, please enter a fruit name: ")

if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy!")
