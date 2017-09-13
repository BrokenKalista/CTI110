# CTI-110 
# M3HW1 - Age Classifier 
# Colleen Moore
# 9/13/17
#
age=int(input('Enter age:'))
def main():
    ageInfant=1
    ageChild=13
    ageTeenager=20
    if age <= ageInfant:
        print('This person is an infant.')
    elif age <= ageChild:
        print('This person is a child.')
    elif age <= ageTeenager:
        print('This person is a teenager.')
    else:
        print('This person is an adult')
main()
