s=[]
r=3
c=3
for i in range(r):
    l=[]
    for j in range(c):       
        n=int(input())
        l.append(n)
    s.append(l)
print(s)
s.sort()
print(s)
s.sort(reverse=True)
print(s)