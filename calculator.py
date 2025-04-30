import math

# TODO: Return tip as well to display.
def calculateTip(subtotal, tip):
    total = subtotal * (tip / 100.0)
    total += subtotal
    return "{:.2f}".format(total)

def calculateCompoundInterest(data):
    annual_rate = data['annual_rate'] / 100
    compound_rate = float(data['compound_rate'])

    interest = 1 + (annual_rate / compound_rate)
    interest = math.pow(interest, compound_rate * data['time'])
    total = data['principal'] * interest
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
