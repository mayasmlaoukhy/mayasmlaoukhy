def fa(p):
    if p==0:
        return f"the factorial of 0 is 1"
    if p<0:
        return "ERROR"
    c=1
    while p>0:
        c*=p
        p-=1
    return c
while True:
    user=input("Enter num to calc factorial: ")
    a=fa(int(user))
    print(a)
    if a=="ERROR":
        break