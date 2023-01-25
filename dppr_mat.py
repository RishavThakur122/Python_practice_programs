#thickness=int(input())
# c='.|.'
length,width=[int(x) for x in input().split()]
str = ".|.";
str2='WEL'
str3='CO'
str4='ME'
length2=int((length+1)/2)
for i in range(length-length2):
      
     print((str*i).rjust(width,'-')+str+(str*i).ljust(width,'-'))
   
     while i==length:
         break;

print(str2.rjust(width,'-')+str3+str4.ljust(width+1,'-'))


for i in reversed(range(length-length2)):
    
    print((str*i).rjust(width,'-')+str+(str*i).ljust(width,'-'))
'''n=int(input())
print("the reversed number are : ",end = "")
for num in reversed(range(n+1)):
    print(num,end = " ")
'''
#soluton iis diffrent as per net you can search it is my version
