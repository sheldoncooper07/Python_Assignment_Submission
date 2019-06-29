#Problem3

#!/bin/python3
adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
x=[]
print("Nos greater than 5 :")
for i in adhoc:
	if i>5:
		print(i)
		x.append(i)
y=[]
print("Nos less than or equal to 2 : ")
for i in adhoc :
	if i <=2 :
		print(i)
		y.append(i)

print("List of nos greater than 5 is :",x)
print("List of nos less than or equal to 2 is :",y)
