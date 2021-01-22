lista=[]
n=int(input("输入个数"))
i=0
while i<n:
    a=int(input("输入一个整数"))
    lista.append(a)
    i=i+1
print("输入结束")
l=len(lista)
for y in range(-1,len(lista)-2):
    p=lista[y]+lista[y+1]
    for q in range(2,p):
        if p%q==0:
            print("\n不是素数")
            c=0
            break
        else:
            c=1
if c:
    print("\n是素数")


