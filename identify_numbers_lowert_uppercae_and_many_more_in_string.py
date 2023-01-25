s = input()    
def has_numbers(inputString):
    print(any(char.isalnum() for char in inputString))
    print(any(char.isalpha() for char in inputString))                                                                         
    print(any(char.isdigit() for char in inputString))
    print(any(char.islower() for char in inputString))
    print(any(char.isupper() for char in inputString))

has_numbers(s) 
