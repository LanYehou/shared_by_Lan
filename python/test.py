def theReturn():
    def funx(x):        #function funx,
        def funy(y):    #function funy is in function funx.
            return(x*y) #return x*y means   now the function funy(y)=x*y . if you   use print(funy(y)) you will get the     answer of x*y .
        return(funy(2)) #now in funy(y) ,   y=2 . So funx(x) = funy(2) = x*2 .
    a=funx(3)   #now in function funx(x),   x=3 . So funx(3) = funy(2) = 3*2 = 6 .
    print(a)    #a=funx(3),so if you use    print(a) , you will get 6.

#if x=3,y=2,the output is 6-.


###########################################################


def algorithm1():
    a=int(input('input a interge between 100~999:\n'))
    m=0
    n=a
    while(n!=0):
        m=m*10+int(n)%10
        n//=10
    print(a,' ==> ',m ,' .\n')


###########################################################

def algo():
    a=1
    b=2
    c= a+b and b-2*a
    print(c)

def algo2():
    a=input('')
    b=1
    c=a+b
    print(c)
def algo3():
    dict={'country':'china','city':'zhangjiang','school':'gdou'}
    print("dict['city']:",dict['city'])

def algo4():
    def ifais0(a):
        if a==0:
            return(0)
        else:
            return(1)
    def output():
        a=1
        if ifais0(a):
            print(a+1)
        else:
            print(a+3)
    output()

def algo5():
    a=1
    b=0
    while a<10:
        b=b+2
        a=a+1
    print(b)

def algo6():
    a=[1,2]
    b=[3,4]
    c=0
    for x in a:
        for y in b:
            c=c+x+y
    print(c)

def algo7():
    a=1
    b=2
    c=0
    def changeab():
        a=3
        b=4
    def addab(a,b):
        c=a+b
        print(c)
    changeab()
    addab(a,b)
    print(a,'\n',b,'\n',c)


if __name__=='__main__':
    algo4()
