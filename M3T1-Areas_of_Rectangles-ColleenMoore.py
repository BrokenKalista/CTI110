# M3T1
# Areas of Rectangle
# Colleen Moore
# 08/27/2017
L1 = int(input('Enter the length of rectangle 1:'))
W1 = int(input('Enter the width of rectangle 1:'))
L2 = int(input('Enter the length of rectangle 2:'))
W2 = int(input('Enter the width of rectangle 2:'))
A1 = L1*W1
A2 = L2*W2
if A1 > A2:
    print('Rectangle 1 has the greater area')
elif A2 > A1:
    print('Rectangle 2 has the greater area')
else:
    print('Both have the same area')
    
