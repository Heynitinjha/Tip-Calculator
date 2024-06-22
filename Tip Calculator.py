print("Welcome To Calculator")
Bill = float(input("Enter the Bill Amount:"))
Tip = int(input("Enter the Tip Amount:"))
Split = int(input("Enter the number of people :"))

Final_Bill = ((Bill+Tip)/Split)

#print(f"Enter the total bill:{Bill}")
#print("Enter the tip amount:"+Tip)
#print("Enter the member:"+Split)

print(f"Your total bill is {Final_Bill}")