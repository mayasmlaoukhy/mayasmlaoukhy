dec=0
l=[]
b=input("enter binary number ")
for i in b:
    l.append(i)
l.reverse()
try:
    for i in range(len(l)):
        dec+=int(l[i])*2**i
    print(dec)
except:
    print("error")
