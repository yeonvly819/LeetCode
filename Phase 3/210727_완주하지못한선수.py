#%%
# trial 1
def solution(participant, completion):

    for i in completion:
        if i in participant:
            participant.remove(i)
    
    answer = participant[0]

    return answer
#%%
# trial 2
def solution(participant, completion):
    
    part_dict = dict()
    
    for i in participant:
        if i in part_dict.keys():
            part_dict[i] += 1
        else:
            part_dict[i] = 1
    
    for j in completion:
        part_dict[j] -= 1
    
    for k, v in part_dict.items():
        if v != 0:
            answer = k
    
    return answer
#%%
# trial 3
from collections import defaultdict

def solution(participant, completion):
    
    part_dict = defaultdict(int)
    
    for i in participant:
        part_dict[i] += 1
    
    for j in completion:
        part_dict[j] -= 1
    
    for k, v in part_dict.items():
        if v != 0:
            answer = k
    
    return answer
#%%
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))