#Problem7

#!/usr/bin/python3
print('''
1. Create a single file
2. Create multiple file
3. Command similar to -c 
''')
option = input('Select an option: ')
if option == '1':
	fname=input("Enter file name")
	f=open(fname+".txt","w+")
	f.close()
if option =='2':
	num=int(input("how many files u wanna create"))
	for i in range(0,num):
	 fname=input("Enter file name")
	 f=open(fname+".txt","w+")
	 f.close()
if option =='3':
	print("You cannot create a file")
