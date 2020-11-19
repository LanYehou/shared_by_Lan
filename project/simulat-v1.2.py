import random
def randchoice(t):
    global a
    i=1
    p=[-0.5,0.5]
    while(i<=int(t)-1):
        a=a+random.choice(p)
        a=a+random.choice(p)
        i=i+1

def addb():
    global b
    b[int(a-1)]=b[int(a-1)]+1

def inputt():
    global t
    try:
        t=int(input('请输入实验次数后按回车键：\n'))
    except:
        check()    
    check()

def check():
    global t
    while type(t) is not int or t<=0:
        try:
            t=int(input('输入错误，请重新输入一个正整数'))
        except:
            continue

t=-1
i=1
b=[0,0,0,0,0,0,0,0,0]
inputt()
while(i<=t):
    a=5
    randchoice(5)
    addb()
    i=i+1
print(b)
