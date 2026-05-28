numbers = [-3, -15, 0, 4, -1]
big=numbers[0]
small=numbers[0]
for num in numbers:
    if num>big:
        big=num
    if num<small:
        small=num
print(big,small)





