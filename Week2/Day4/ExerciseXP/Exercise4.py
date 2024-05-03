
def compare_numbers(user_number):
    if not 1 <= user_number <= 100:
        return "Please enter a number between 1 and 100."

    random_number = random.randint(1, 100)

    if user_number == random_number:
        return "Congratulations! You guessed the right number."
    else:
        return f"Oops! You guessed {user_number}, but the random number was {random_number}."

user_input = int(input("Enter a number between 1 and 100: "))
result = compare_numbers(user_input)
print(result)
