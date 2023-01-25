value=0
year=int(input("give a year :"))
if year%100==0:
    print("year is divisible by 100")
    value=year%400
    if value==0:
        print("it is an leap year ")
    else:
        print("not a leap year")
else:
    print("year is not divisible by 100")
    value=year%4
    if value==0:
        print("leap")
    else:
        print("not leap")
    
    
