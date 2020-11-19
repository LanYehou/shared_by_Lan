def funx(x):        #function funx,
    def funy(y):    #function funy is in function funx.
        return(x*y) #return x*y means   now the function funy(y)=x*y . if you   use print(funy(y)) you will get the     answer of x*y .
    return(funy(2)) #now in funy(y) ,   y=2 . So funx(x) = funy(2) = x*2 .
a=funx(3)   #now in function funx(x),   x=3 . So funx(3) = funy(2) = 3*2 = 6 .
print(a)    #a=funx(3),so if you use    print(a) , you will get 6.

#if x=3,y=2,the output is 6-.

def algorithm1():
    a=int(input('input a interge between 100~999:\n'))
    m=0
    n=a
    while(int(n)!=0):
        m=m*10+int(n)%10
        n/=10
    print(a,' ==> ',m ,' .\n')

if __name__=='__main__':
    algorithm1()
