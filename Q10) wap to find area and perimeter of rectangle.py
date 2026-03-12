# wap to find area and perimeter of rectangle
length = float(input("Enter length of the rectangle"))
width = float(input("Enter width of the rectangle"))

area = length*width
perimeter = 2*(length+width)

print(f"specifications of rectangle is {length} by {width}")
print("its perimeter is : ",perimeter)
print("its area is : ",area)