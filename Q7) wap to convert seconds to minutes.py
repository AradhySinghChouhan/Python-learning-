# wap to convert seconds to minutes
total_sec = int(input("enter total no of secounds"))
minutes = int(total_sec / 60)   #calculate minutes
remaning_sec = total_sec % 60 #calculate secounds
print(f"{total_sec} secounds is {minutes} minutes and {remaning_sec} seconds")
