length,width=[int(x) for x in input().split()]
str = ".|.";
str2='WEL'
str3='CO'
str4='ME'
length2=int((length+1)/2)
for i in range(length-length2):
      
     print((str*i).center(width,'-'))
   
     while i==length:
         break;

print(str2.rjust)


for i in reversed(range(length-length2)):
    
    print((str*i).rjust(width,'-')+str+(str*i).ljust(width,'-'))
