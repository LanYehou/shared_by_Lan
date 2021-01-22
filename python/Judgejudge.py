
print ("the judge ask the criminal : Do you admit your crime?")
yes = "yes"
no = "no"
a = str(input("A say: (please enter 'yes' or 'no')"))
b = str(input("B say: (please enter 'yes' or 'no')")) 

while a == 'yes' and b == 'yes' :
	print ('A and B all 10 years')
	break
while a == 'yes' and b == 'no' :
	print ('A 1 year, B 20 years')
	break
while a == 'no' and b == 'yes' :
        print ('A 20 year, B 1 years')
	break
while a == 'no' and b == 'no' :
        print ('A 3 year, B 3 years')
	break
