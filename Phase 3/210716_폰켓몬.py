#%%
# 1st trial
import itertools
def solution(nums):

    pick_n = int(len(nums)/2)

    comb = list(itertools.combinations(nums, pick_n))

    max_mon = 0
    mon_count = [len(set(i))for i in comb]
    max_mon = max(mon_count)        

    answer = max_mon
    return answer
#%%
# 2nd trial
def solution(nums):
    answer = 0

    pick_num = int(len(nums)/2) # the number of ponkemons to be picked

    unique_mon = len(set(nums)) # the number of unique ponkemons

    if unique_mon > pick_num:
        answer = pick_num # you cannot pick the number of ponkemons more than pick_num
    else:
        answer = unique_mon # this is the maximum unique_mon you can pick
    
    return answer
#%%
print(solution([3, 1, 2, 3]))