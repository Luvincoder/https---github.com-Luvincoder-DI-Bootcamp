def generate_multiples(num, length):
    multiples = []
    current_multiple = num
    while len(multiples) < length:
        multiples.append(current_multiple)
        current_multiple += num
    return multiples

number = int(input("Enter a number: "))
length = int(input("Enter the length: "))


result = generate_multiples(number, length)
print(result)