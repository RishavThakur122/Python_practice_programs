def count_substring(string, sub_string):
    total=0
    for i in range (len(string)):
        if string[i:].startswith(sub_string):
            total+=1
        #c=string.count(sub_string)
    return total


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
