# CTI-110 
# M3HW2 - Software Sales 
# Colleen Moore
# 9/13/17
#
quantity=int(input('Enter number of packages sold: '))
overallPrice = quantity * 99
def main():
    tenPercent=19
    twentyPercent=49
    thirtyPercent=99

    if quantity <= tenPercent:
        print('You have received a 10% discount, your new price is $',overallPrice)
    elif quantity <= twentyPercent:
        print('You have received a 20% discount, your new price is $',overallPrice)
    elif quantity <= thirtyPercent:
        print('You have received a 30% discount, your new price is $',overallPrice)
    else:
        print('You have received a 40% discount, your new price is $',overallPrice)

main()
