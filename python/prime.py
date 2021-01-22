def isprime(a):
    n=1
    k=int(a**(1/2))+1
    for i in range(2,k):
        if a%i==0:
            n=0
    return n
print('请输入：')
while True:
    try:
        a = input()
        arr = [int(n) for n in a.split()]
        arr.append(arr[0])
        n=1
        for i in range(len(arr)-1):
            s = arr[i]+arr[i+1]
            if isprime(s)==0:
                n=0
        if n==0:
            print('不是素数环')
        else:
            print('是素数环')
        break
    except:
        print('输入错误！\n请重新输入：')
