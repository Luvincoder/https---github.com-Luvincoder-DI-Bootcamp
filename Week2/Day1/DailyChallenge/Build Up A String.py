
while True:
    user_input = str( input("Enter a string: "))
    if len(user_input) < 10:
        print("String not long enough.")
    elif len(user_input) > 10:
        print("String too long.")
    else:
        print("Perfect string.")
    