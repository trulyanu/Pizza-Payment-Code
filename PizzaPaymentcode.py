print("Welcome to the Pizza House")
size= input("What size of pizza do you want?? S M L")
pepperoni= input("Do you want pepperoni on top?? Y N")
Extra_cheese= input("Do you want extra cheese?? Y N")
bill=0
bill1=0
bill2=0
Total_bill=0
if size== "S":
    bill= 15
    print("You have ordered a Small size pizza")
    if pepperoni == "Y":
        bill1= 3
    print("You have added pepperomi in your pizza")
    if  Extra_cheese == "Y":
        bill2 = 1
    print("You have added Cheese in your pizza")
    Total_bill= bill+bill1+bill2
elif size== "M":
    bill= 20
    print("You have ordered a Medium size pizza")
    if pepperoni == "Y":
        bill1= 5
    print("You have added pepperomi in your pizza")
    if  Extra_cheese == "Y":
        bill2 = 1
    print("You have added Cheese in your pizza")
    Total_bill= bill+bill1+bill2
else:
    bill = 30
    print("You have ordered a Large size pizza")
    if pepperoni == "Y":
        bill1 = 5
    print("You have added pepperomi in your pizza")
    if Extra_cheese == "Y":
        bill2 = 1
    print("You have added Cheese in your pizza")
    Total_bill = bill + bill1 + bill2
print(f"So Your total billable amount is {Total_bill} Rupees ")
print("Thank you Visit Again")
print("Have a GREAT DAY")
print("From PIZZA HOUSE")

