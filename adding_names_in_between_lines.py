def print_full_name(first,last):
    TXT="Hello {} {} !you just delved into python"
    print(TXT.format(first,last))
            
    
   
if __name__=='__main__':
    firsr_name = input()
    last_name = input()
    print_full_name(first_name,last_name)

'''def print_name(name):
    txt="hello {} !"
    print(txt.format(name))
if __name__=='__main__':
    a=input("whtas your name :")
    print_name(a)'''
