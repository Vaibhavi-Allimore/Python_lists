numbers=[10,5,20,15,20,12]
print("list:",numbers)
unique=[]
for x in numbers:
    if x not in unique:
        unique.append(x)
print("Unique values:",unique)
