# -*- coding:utf-8 -*-
run = '1'

def computAndPrint(m,z):
	global run
	p = 3.14*m
	ha = m
	hf = 1.25*m
	h = 2.25*m
	d = m*z
	da = m*(z+2)
	df = m*(z-2.5)
	print ('---------------------------+\n\
齿距p  =%-19s|\n\
齿顶高ha =%-17s|\n\
齿底高hf =%-17s|\n\
齿高h =%-20s|\n\
分度圆直径d =%-14s|\n\
齿顶圆直径da =%-13s|\n\
齿根圆直径df =%-13s|\n\
---------------------------+'%(str(p),str(ha),str(hf),str(h),str(d),str(da),str(df)))
	run=input('1 :新的计算。\n\
2 :计算与当前齿轮相配合的齿轮尺寸。\n\
3 :退出。\n\
----------------------------\n\
请输入序号1~3来选择您需要的操作。\n\
>>>')

	while run!='1' and run!='2' and run!='3':
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\
！！！输入的序号无效！！！\n\
!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\
请务必输入序号1~3来选择您需要的操作。\n')
		run = input ('1 :新的计算。\n\
2 :计算与当前齿轮相配合的齿轮尺寸。\n\
3 :退出。\n\
----------------------------\n\
请输入序号1~3来选择您需要的操作。\n\
>>>')


while run=='1' or run=='2' :
	if run == '1':
		print ('----------------------------\n\
标准直齿轮基本尺寸计算器\n\
输入模数和齿数来计算其他尺寸\n\
输入后按回车键\n\
(π取3.14)\n\
----------------------------')
		while True :
			try :
				m = float(input ('>>>输入模数m= :'))
				z = float(input ('>>>输入齿数z= :'))
				break
			except ValueError:
				print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\
！！！请务必输入整数！！！\n\
!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		computAndPrint(m,z)
	
	elif run == '2':
		while True :
			try :
				a = float(input ('>>>输入两齿轮中心距a= :'))
				break
			except ValueError:
				print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\
！！！请务必输入整数！！！\n\
!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		z = (2*a)/m-z
		computAndPrint(m,z)

