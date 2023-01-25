if __name__ == '__main__':
    n = int(input())
    student_marks = {}  
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
student_scores=list(student_marks[query_name])
ans=sum(student_scores)
average=ans/n
print(average)
    
"""if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
output = list(student_marks[query_name])    
per = sum(output)/len(output);
print("%.2f" % per);"""    
