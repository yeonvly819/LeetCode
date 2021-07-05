#%%
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
#%%
print(solution('1D#2S*3S'))