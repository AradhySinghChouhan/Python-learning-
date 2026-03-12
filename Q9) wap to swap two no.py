#wap to swap two numbers in python
a = int(input("enter first number :"))
b = int(input("enter secound number :"))

print("before swapping")
print("first = ",a)
print("secound = ",b)

temp = a
a = b
b = temp

print("after swapping : ")
print("first = ",a)
print("secound = ",b)
