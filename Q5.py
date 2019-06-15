#Problem5
#!/bin/python3
import datetime

name =input("what is ur name?")
d=datetime.datetime.now()
h=d.hour
if h<12:
	print("Good Morning",name+"!")
elif h>11 and h<=17:
	print("Good Afternoon",name+"!")
elif h > 17 and h <=20:
	print("Good Evening",name+"!")
else:
        print("Good Night", name+"!")
