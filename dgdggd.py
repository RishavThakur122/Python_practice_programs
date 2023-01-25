count=0
for i in range(1947,2021):
    if(i%400==0 or i%100!=0 and i%4==0):
        count=count+1
        print("leap : ",i)
print("number of leap years : ",count)
        
