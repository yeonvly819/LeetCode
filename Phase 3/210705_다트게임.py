#%%
# 2nd try
import re
def solution(dartResult):
    answer = 0

    score_split = re.compile('\d+[A-Z][*#]?').findall(dartResult)

    score = []

    for i in score_split:
        num = int(re.compile('\d+').findall(i)[0])
        section = re.compile('[A-Z]').findall(i)[0]
        reward = re.compile('[*#]+').findall(i)
        
        if section == 'D':
            num = num ** 2
        
        elif section == 'T':
            num = num ** 3
        
        if len(reward) == 0:
            pass
        
        elif reward[0] == '*':
            num *= 2
            if len(score) >= 1:
                score[-1] = score[-1] * 2
        
        elif reward[0] == '#':
            num = num * (-1)

        score.append(num)

    answer = sum(score)

    return answer
#%%
print(solution('1D2S#10S'))
#%%
# 1st try
def solution(dartResult):
    answer = 0

    score = []

    for i in dartResult:
        if i.isdigit():
            score.append(i)
    
        elif i == 'S':
            score[-1] = str(int(score[-1]) ** 1)

        elif i == 'D':
            score[-1] = str(int(score[-1]) ** 2)

        elif i == 'T':
            score[-1] = str(int(score[-1]) ** 3)

        elif i == '*':
            if len(score) > 1:
                score[-2] = str(int(score[-2]) * 2)
                score[-1] = str(int(score[-1]) * 2)
            
            else:
                score[-1] = str(int(score[-1]) * 2)
        
        elif i == '#':
            score[-1] = str(int(score[-1]) * (-1))
    
    answer = sum(map(int, score))

    return answer