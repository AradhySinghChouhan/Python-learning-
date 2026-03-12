str1 = "this is a string"
str2 = '\n this is also a string' #next line
str3 = """\t this is too""" #tab space

print(str1 ,str2,str3)

name ="Aradhy"
surname = "Singh"
full_name = name+" "+surname+" "+"Chouhan"
print(name + surname)
print(full_name)

print(len(full_name))

#indexing 
print(full_name[5])
c = full_name[2]
print(c)

#slicing
#positive
print(full_name[0:6])
print(full_name[7:len(full_name)])
print(full_name[13:])
print(full_name[:6])
#negetive
print(full_name[-13:-7])

#string funtion
print(full_name.endswith("uhan"))
print(full_name.capitalize())
print(full_name.replace("Aradhy","Vinod"))
print(full_name.find("i"))
print(full_name.count("h"))
# there are many more sring functions