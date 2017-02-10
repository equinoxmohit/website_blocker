import time
from datetime import datetime as dt

host_path='/etc/hosts' #location for host file
redirect="127.0.0.1"
website_list=[] #websites to block
print("list website to block")
number=int(input()) #use try except and declare the variable if it doesn't work

while number!=0:
	print("enter domain to block:")
	web=input()
	website_list.append(web)
	number -=1

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 5,30) <  dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 8,00):
            print ("time")

            with open(host_path,'r+') as file:
                content=file.read()
                print(content)

                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write(redirect+" "+website+"\n")
    else:
            with open(host_path,'r+') as file:
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
                print("total_time")

    time.sleep(15)
