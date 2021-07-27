#%%
def solution(s):
    
    answer = ''
    res = ''
    
    num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 
                'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

    for i in s:
        if i.isdigit():
            answer += str(i)
        else:
            
            res += i
            if res in num_dict:
                answer += str(num_dict[res])
                res = ''

    answer = int(answer)            

    return answer
#%%
print(solution("one4seveneight"))