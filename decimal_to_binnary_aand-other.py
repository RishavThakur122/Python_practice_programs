def print_formatted(n):
    for i in range(1,n+1):
       if(i >= 1):
# divide with integral result
# (discard remainder)
           decimalToBinary(n//2)
       print(n%2, end=' ')


if __name__== '__main__':
    dec_val=int(input())
    print(print_formatted(dec_val))
