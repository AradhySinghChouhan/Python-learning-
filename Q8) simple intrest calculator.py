#wap to calculate SI with P,I,T input
pri_amt = float(input("enter amount to borrow : "))
intrest = int(input("enter interst rate on amount : "))
time = int(input("enter time of loan in years : "))
SI = (pri_amt*intrest*time)/100
print(f"total interst on amount = {pri_amt} with {intrest}% rate in {time} years is :{SI}")