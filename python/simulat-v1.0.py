import os
import random
i=1
n=1
a=5
b=[0,0,0,0,0,0,0,0,0]
p=[-0.5,0.5]
t=int(input('请输入实验次数后按回车键：\n'))
while(i<=t):
    while(n<5):
        a=a+random.choice(p)
        a=a+random.choice(p)
        n=n+1
    b[int(a-1)]=b[int(a-1)]+1
    a=5
    n=1
    i=i+1
print(b)
os.system("pause")
