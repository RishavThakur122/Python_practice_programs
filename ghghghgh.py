l1=[1,1,1,1,1,1,1,1,2,2,2,21,1,3,3,3]
l2=[*set(l1)]
l3=[]
print(l2)
for i in l2:
    l3.append(l1.count(i))
print(l3)
ini=l3.index(max(l3))
print(l2[ini])
