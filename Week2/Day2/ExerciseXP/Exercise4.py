start = 1.5
step=0.5
count=8
sequence=[start + (step * i) for i in range(count)]
print(*sequence,sep=", ")
# print(sequence)