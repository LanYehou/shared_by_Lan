lista = []

def printusage():
    print('请输入多个整数，每输入完一个数按回车后继续输入下一个数。\n\
输入为空时(不输入，直接按回车键)结束输入。')

def getlist():
    global lista
    a=1
    i=1
    while(a!=''):
        print('请输入一个整数: (第',i,'个数)')
        a=input()
        if (a==''):
            print('输入结束。共',i-1,'个数.')
            return('done')
        else:
            try:
                a=int(a)
                lista.append(a)
                i=i+1
            except:
                print('输入错误!\n')
                continue

def isprime(lista):
    n=2
    for i in range(-1,len(lista)-2) :
        p=lista[i]+lista[i+1]
        while n<p  :
            if not p%n:
                return(0)
            n=n+1
    return(1)

if __name__=='__main__':
    printusage()
    getlist()
    if isprime(lista):
        print(lista,' 是素数环。')
    else:
        print(lista,' 不是素数环。')
