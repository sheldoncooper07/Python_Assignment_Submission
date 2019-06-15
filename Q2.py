#Problem2
#!/usr/bin/python3
import webbrowser 
from googlesearch import search
import time
web=input('enter the topic u wanna search:')

list= []
for i in search(web,stop=10):
	print(i)
	time.sleep(3)
	list.append(i)
print(list)
f = open('url.txt','a+')
for i in list:
	f.write(i+'\n')
f.close()
