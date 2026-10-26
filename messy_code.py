# ORIGINAL MESSY VERSION (kept for comparison)
def f(l):
    t=0
    for i in range(0,len(l)):
        t=t+l[i]
    a=t/len(l)
    return a
def g(a):
    if a>=90:
        return "A"
    else:
        if a>=80:
            return "B"
        else:
            if a>=70:
                return "C"
            else:
                if a>=60:
                    return "D"
                else:
                    return "F"
n=input("enter name")
m=[]
x=int(input("how many subjects"))
for i in range(0,x):
    y=int(input("marks"))
    m.append(y)
r=f(m)
print(n,"average is",r,"grade is",g(r))
if max(m)==m[0]:print("best subject is 1")
