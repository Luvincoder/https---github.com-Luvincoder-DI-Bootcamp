import string
import random

def generate_random_string(length=5):
    letters = string.ascii_letters   
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


random_str = generate_random_string()
print(random_str)
