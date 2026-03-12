#to check a letter is vowel or nor
str = str(input("enter a single letter : "))

if(len(str)==1):
    if(str=="a"or str=="e"or str=="i"or str=="o"or str=="u"):
        print(f"{str} is a vowel")
    else:
        print(f"{str} is not a vowel")
else:
    print("invalid input\n program terminated")        