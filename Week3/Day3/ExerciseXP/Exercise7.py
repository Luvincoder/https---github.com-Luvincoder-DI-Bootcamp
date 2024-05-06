from faker import Faker


fake = Faker('en_US')  


users = []

def add_fake_user():
    
    fake_name = fake.name()
    fake_address = fake.address()
    fake_language_code = fake.language_code()

    user_data = {
        'name': fake_name,
        'address': fake_address,
        'language_code': fake_language_code
    }


    users.append(user_data)


for _ in range(5):
    add_fake_user()


print(users)
