
print("welcome to the tip calculator")
bill =float( input("What was your total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people =int(input("How many people to split the bill? "))
tip2 = bill *  tip / 100
total_bill = bill + tip2
per_person = round(total_bill / people,2)
print(f"Each person should pay: ${per_person}")

