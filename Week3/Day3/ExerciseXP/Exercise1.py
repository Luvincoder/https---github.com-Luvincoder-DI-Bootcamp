class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        elif isinstance(other, Currency) and self.currency == other.currency:
            return Currency(self.currency, self.amount + other.amount)
        else:
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency) and self.currency == other.currency:
            self.amount += other.amount
        else:
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        return self

# Testing the Currency class with the given scenarios
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))  # '5 dollars'
print(int(c1))  # 5
print(repr(c1))  # '5 dollars'

print(c1 + 5)  # 10
print(c1 + c2)  # 15

print(c1)  # 5 dollars

c1 += 5
print(c1)  # 10 dollars

c1 += c2
print(c1)  # 20 dollars

try:
    print(c1 + c3)
except TypeError as e:
    print(e)  
