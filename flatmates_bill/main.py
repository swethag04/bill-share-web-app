from flat import Bill, Flatmate
from report import PdfReport

bill_amt = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? Eg. March 2024: ")
name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period?"))
name2 = input("What is the name of other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period?"))

bill_amount = Bill(amount=bill_amt, period = period)
flatmate1 = Flatmate(name= name1, days_in_house = days_in_house1)
flatmate2 = Flatmate(name= name2, days_in_house= days_in_house2)

flatmate1_share = str(round(flatmate1.pays(bill_amount, flatmate2),2))
flatmate2_share = str(round(flatmate2.pays(bill_amount, flatmate1),2))

print(f"{name1} pays: ",flatmate1_share)
print(f"{name2} pays: ",flatmate2_share)

pdfreport = PdfReport('bill.pdf')
pdfreport.generate(flatmate1, flatmate2, bill_amount)