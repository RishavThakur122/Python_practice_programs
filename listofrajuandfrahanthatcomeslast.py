# Nested Lists in Python - Hacker Rank Solution  
# python2 solution
score_list = []; # do not forget to declare a list
for _ in range(int(input())):
    name = input()
    score = float(input())
    
    # Nested Lists in Python - Hacker Rank Solution START
    score_list.append([name, score])
second_highest = sorted(set([score for name, score in score_list]))[1]
print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))
# Nested Lists in Python - Hacker Rank Solution END

        
