
while True:
    user_input = input("Enter a string (must be 'abcdefghij'): ")
    if user_input != 'abcdefghij':
        print("Incorrect string entered.")
    elif len(user_input) < 10:
        print("String not long enough")
    