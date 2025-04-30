import math

# TODO: Return tip as well to display.
def calculateTip(subtotal, tip):
    total = subtotal * (tip / 100.0)
    total += subtotal
    return "{:.2f}".format(total)

def calculateCompoundInterest():
    principal = float(input("enter principal: "))
    interest_rate = float(input("enter interest rate: "))
    compound_rate = float(input("enter compound rate: "))
    time = float(input("enter time in years: "))
    total = principal * math.pow((1 + interest_rate / compound_rate), compound_rate * time)
    return "{:.2f}".format(total)

def calculateInternshipPay():
    weeks = int(input("enter number of weeks: "))
    hours = int(input("enter number of hours per week: "))
    rate = float(input("enter pay rate per hour: "))
    total = rate * hours * weeks
    return "{:.2f}".format(total)

# print(calculateTip())
# print(calculateInternshipPay())
# print(calculateCompoundInterest())
