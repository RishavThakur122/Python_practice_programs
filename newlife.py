s= "   fly me   to   the moon  "
print(len(s))
i=0
count=0
for i in range(len(s)):
    if s[i]!=" ":
        break
print(i)
while s[i]==" ":
    count=count+1
print(count)
