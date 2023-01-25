nums=[0,1,0,3]
temp=nums.count(0)
for i in range(temp):
    nums.remove(0)
print(nums)
print(temp)
for i in range(temp):
    nums.append(0)
print(nums)
