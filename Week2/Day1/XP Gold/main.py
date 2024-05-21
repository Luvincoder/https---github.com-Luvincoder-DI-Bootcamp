
#exercise 1


# print("Hello world\n" * 4 + "I love python\n" *4)


#exercise 2

User_month = int(input("Enter your month number 1 to 12: " ))
if User_month in [3, 4, 5] :
    print("You are in spring season.")
elif User_month in [6, 7, 8] :
    print("You are is summer season.")
elif User_month in [9, 10, 11] :
    print("you are in Autumu season.")
elif User_month in [12, 1, 2] :
    print("you are is winter season.")
else:
    print("You enter a wrong number")
