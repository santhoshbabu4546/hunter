sh=int(input())
k1=0
lst=input().split()
lst=list(map(int,lst))
new=[]
for i in range(0,sh):
    if((lst.count(lst[i]))>=2):
      if lst[i] not in new:
        new.append(lst[i])
        k1=1
if(k1==0):
  print("unique")
else:
  for i in range(0,sh):
    print(min(new),end=" ")
    new.remove(min(new))
