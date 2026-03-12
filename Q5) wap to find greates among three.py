# find the greatest number in three 
first = int(input("enter first number"))
secound = int(input("enter secound number"))
third = int(input("enter third number"))

if(first > secound and first > third):
    print(f"{first} is the gratest number")

elif(first > secound and first > third):
    print(f"{secound} is the gratest number")

else:
    print(f"{third} is the gratest number")