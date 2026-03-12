#wap to grade student according to marks
marks = int(input("enter your marks "))
grade = "none"
if(marks >= 90):
    if(marks > 100):
        print("invalid input")
    else:
        grade = "A"    
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"       
else:
    grade = "D"

print("grade of the student is :",grade)     