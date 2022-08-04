print("Welcome to the tip calculator")

#input total bill
total_bill = float(input("what was the total bill? $"))

#input the tip percentage
tips = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

#input the total no of people
no_of_people = int(input("How many people to split the bill? "))

#calculate total bill with tip
bill_with_tip = (total_bill * tips / 100) + total_bill

#calculate bill for each person
bill_per_person = bill_with_tip / no_of_people

#each_pay_bill = round(bill_per_person,2), it would give 33.6, but we need 33.60
#so, we use format to get uptp 2 decimal places
each_pay_bill = "{:.2f}".format(bill_per_person)

#printing each person bill using f-string
print(f"Each person should pay: ${each_pay_bill}")

