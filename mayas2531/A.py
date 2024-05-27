L1=['HTTP','HTTPS','FTP','DNS']
L2=[80,443,20,53]
d={}
for i in L1:
    d[i]=L2[L1.index(i)]
print(d)
