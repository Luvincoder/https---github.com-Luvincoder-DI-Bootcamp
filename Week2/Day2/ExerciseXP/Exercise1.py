my_fav_numbers = {17, 22, 30, 50}
#print(my_fav_numbers)

my_fav_numbers.add(5)
my_fav_numbers.add(15)
#print(my_fav_numbers)

my_fav_numbers.remove(30)
#print(my_fav_numbers)

friend_my_fav_numbers = {20, 25, 65, 80}
our_fav_numbers = my_fav_numbers.union(friend_my_fav_numbers)

print(our_fav_numbers)



