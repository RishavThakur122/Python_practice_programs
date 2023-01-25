startyear=int(input("enter the first year : "))
endyear=int(input("enter the last year : "))
for  i in range(startyear,endyear+1):
    if i%4==0 and i%100!=0 or i%400==0:
        print(i)
