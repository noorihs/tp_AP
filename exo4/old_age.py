age1 = int(input("Please type in the age of the first person:"))
age2 = int(input("Please type in the age of the second person:"))

if age1 > age2:
    print("The older age is:", age1)
elif age2 > age1:
    print("The older age is:", age2)
else:
    print("Both people are the same age!")
