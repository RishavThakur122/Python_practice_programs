def checkmoney(number):
    if number<7000:
        print("Ahem, can you rethink this number please?")
    elif number>10000:
        print("Wow sis!you are queen")
    elif number>=7000 or number<=10000:
        print("Cool, thanks sis! {} rupees will help".format(number))
        
        
sis=8500
checkmoney(sis)
