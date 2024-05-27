file="1.txt"
infile=open(file,'r')
s=infile.read()
l=s.split()
infile.close()
c=0
for i in l:
    print(i[:-1])
    s=input()
    if s==i[-1]:
        c+=1
user=input("enter your name ")
s=user+","+str(c)+",from 20"
print(s)
out=open("2.csv",'w')
out.write(s)
out.close()
