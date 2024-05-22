family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

cost_per_member = {}

for name, age in family.items():
    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15
    
    cost_per_member[name] = cost
    total_cost += cost

for name, cost in cost_per_member.items():
    print(f"{name.capitalize()} has to pay ${cost}")

print(f"The total cost for the family is ${total_cost}")