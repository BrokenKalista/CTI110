#CTI-110
#M2HW2-Tip Tax Total
#Colleen Moore
#8/24/2017
foodCost = float(input('How much did your meal cost? '))
tipAmount = foodCost * .18
salesTax = foodCost * .07
totalCost = foodCost + tipAmount + salesTax
print('Total Cost:' , format(totalCost, ',.2f'))
print('Sales Tax:' , format(salesTax, ',.2f'))
print('Tip:' , format(tipAmount, ',.2f'))
