s=int(input())
n=list(map(int,input().split(None,s)[:s]))
s=[]
for i in range(len(n)):
    if n[i]==i:
        
        s.append(n[i])
if len(s)==0:
    print(-1)
else:
    print(" ".join(map(str,s)))
