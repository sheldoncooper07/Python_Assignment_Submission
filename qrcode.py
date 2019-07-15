#QR_CODE

#!/usr/bin/python3

from googlesearch import search 
import pyqrcode
from pyqrcode import QRCode

urlinput=input("Enter the text to search")
urllist=[]
for i in search(urlinput, tld='com', lang='en', num=10, start=0, stop=5, pause=2) :
	urllist.append(i)
	print(i)
	url=pyqrcode.create(i)
	for j in range(5) :
		url.svg(str(j)+".svg",scale=8)
		print(url.terminal())
