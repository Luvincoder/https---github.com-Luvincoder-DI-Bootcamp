import matplotlib.pyplot as plt


# x = [1, 2, 3, 4, 5]  # Prices
# y = [5, 4, 3, 2, 1]  # Demand


# plt.figure(figsize=(8, 6))
# plt.plot(x, y, marker='o')
# plt.title("Demand for a Product at Different Price Points")
# plt.grid(True)
# plt.show()

# # ----------3

# x = [1, 2, 3, 4, 5]  # Age
# y = [75, 80, 88, 95, 105]  # Height in cm


# plt.figure(figsize=(8, 6))
# plt.scatter(x, y, color='blue')
# plt.grid(True)
# plt.show()

# #----------4

# x = [1, 2, 3, 4, 5]  # Prices
# y = [5, 4, 3, 2, 1]  # Demand


# plt.figure(figsize=(8, 6))
# plt.plot(x, y, marker='o')
# plt.title("Product Demand vs Price")
# plt.xlabel("Price")
# plt.ylabel("Demand")
# plt.grid(True)
# plt.show()
# # plt.savefig("myPng.png")

# #-------------5


# x = [1, 2, 3, 4, 5]  # Age
# y = [75, 80, 88, 95, 105]  # Height in cm


# plt.figure(figsize=(8, 6))
# plt.scatter(x, y, color='blue')
# plt.title("Children's Height vs Age")
# plt.xlabel("Age (years)")
# plt.ylabel("Height (cm)")
# plt.grid(True)
# plt.show()
# # plt.savefig("myPng2.png")

# #----------------6

import numpy as np

x = np.linspace(-10, 10, 1000)
y1 = np.sin(x)


# plt.figure(figsize=(10, 6))
# plt.plot(x, y1, label='sin(x)', color='tab:blue')
# plt.xlabel("x")
# plt.ylabel("sin(x)")
# plt.legend()
# plt.grid(True)
# plt.show()


# plt.figure(figsize=(10, 6))
# plt.scatter(x, y1, label='sin(x)', color='tab:blue', marker='o')
# plt.xlabel("x")
# plt.ylabel("sin(x)")
# plt.legend()
# plt.grid(True)
# plt.show()


#------------


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))


ax1.plot(x, y1, label='sin(x)', color='tab:blue')
ax1.set_title("Sine Function Line Plot")
ax1.set_xlabel("x")
ax1.set_ylabel("sin(x)")
ax1.legend()
ax1.grid(True)


ax2.scatter(x, y1, label='sin(x)', color='tab:blue', marker='o')
ax2.set_title("Sine Function Scatter Plot")
ax2.set_xlabel("x")
ax2.set_ylabel("sin(x)")
ax2.legend()
ax2.grid(True)


plt.tight_layout()
plt.savefig("sine_function_subplots.png")
plt.show()


grades = [88, 90, 95, 92, 88, 90, 88, 85, 93, 92, 90, 87, 95, 90, 88]

plt.hist(grades, bins=5, edgecolor='black')  
plt.xlabel('Grades')
plt.ylabel('Frequency')
plt.title('Distribution of Grades in a Class')
plt.show()





