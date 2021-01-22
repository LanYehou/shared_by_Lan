def typeof(variate):
    type1=""
    if type(variate)==type(1):
        type1="int"
    else:type1="对不起，输入错误，请输入整数"
    return type1

b=input("请问您需要输入多少个整数")
a=0
for i in range(int(b)):
    N=input("请输入一个整数")
# N定义后，就是字符串格式，不知道该怎么区分，我只知道分辨数据类型的代码（列在上面了）
    if int(N)%2==0:
        a=a+1
print("输入结束，共",b,"个数。")
if a==int(b)/2:
    print("这",b,"个数可以组成素数环。")
else:print("这",b,"个数不可以组成素数环。")
