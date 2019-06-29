#Problem7
#!/usr/bin/python3
import subprocess
import os
command=input('Enter a linux command: ')
f=open('Command.txt','a+')
f.seek(0)
data=f.read()
s=subprocess.getstatusoutput(command)

if command in data:
	os.system('echo Do not enter repeated command | festival --tts')
else:
	f=open('Command.txt','a+')
	f.write(command)
	f.write('\n')
	f.close()

	if s[0]==0:
		os.system(command)
	else:
                os.system('echo Incorrect command | festival --tts') 
