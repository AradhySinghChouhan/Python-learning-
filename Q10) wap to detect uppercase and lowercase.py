# to check wheather no is a uppercase or a lowercase
letter = str(input("enter a single letter : "))

if(len(letter)==1):
    if("A" <= letter <= "Z"):
        print(f"{letter} is in uppercase")
    elif("a" <= letter <= "z"):
        print(f"{letter} is in lowercase")
else:
    print("invaild input")        