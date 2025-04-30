import math

def calculateTip(data):
    tip = data['subtotal'] * (float(data['tip']) / 100)
    total = data['subtotal'] + tip
    return "{:.2f}".format(tip), "{:.2f}".format(total)

def calculateCompoundInterest(data):
    annual_rate = data['annual_rate'] / 100
    compound_rate = float(data['compound_rate'])

    interest = 1 + (annual_rate / compound_rate)
    interest = math.pow(interest, compound_rate * data['time'])
    total = data['principal'] * interest
    return "{:.2f}".format(total)

def calculateInternshipPay(data):
    total = data['hourly_rate'] * data['hours'] * data['weeks']
    return "{:.2f}".format(total)
