def swap_case(s):
    a=''
    for char in s:
        if (char.isupper())==True:
            a+=(char.lower())
        elif (char.islower())==True:
            a+=(char.upper())
        elif  (char.isspace())==True:
            a+='-'
    return a    
        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
'''def swap_case(s):

    # sWAP cASE in Python - HackerRank Solution START
    Output = '';
    for char in s:
        if(char.isupper()==True):
            Output += (char.lower());
        elif(char.islower()==True):
            Output += (char.upper());
        else:
            Output += char;
    return Output;
    # sWAP cASE in Python - HackerRank Solution END

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)'''
