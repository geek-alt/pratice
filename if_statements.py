age = int(input("Enter the age: "))

if age >=100:
    print("You are too old for signing up the membership account")
elif age >= 18:
    print("You have successfully got your credit card")
elif age < 0:
    print("You haven't been born yet!!")
else:
    print("Sorry, your are not 18 years old.")