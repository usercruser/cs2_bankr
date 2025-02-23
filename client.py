import os
import subprocess
print("==== 서버 피커 ====\n1 : 한국서버 차단\n2 : 한국서버 차단 해제\n3 : 종료")
a = int(input("~$ "))
if a == 1:
    os.getcwd()
    dir=open("data")
    subprocess.call([r'client.bat'])
elif a == 2:
    os.getcwd()
    dir=open("data")
    subprocess.call([r'client1.bat'])
else:
    exit()