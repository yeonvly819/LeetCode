#%%
from itertools import combinations
from collections import defaultdict

def solution(orders, course):

    answer = []
    orders = [sorted(o) for o in orders]
    
    order_combs = []
    order_dict = defaultdict(int)

    for i in orders:
        for j in range(2, len(i) + 1):
            order_combs.append(list(combinations(i, j)))
    
    for i in range(len(order_combs)):
        for j in order_combs[i]:
            order_dict[j] += 1
    
    # order_dict = sorted(order_dict.items(), reverse=True, key=lambda item: item[0])

    result = list()

    for c in course:
        temp = list()
        for k, v in order_dict.items():
            if c == len(k):
                temp.append([k, v])
        if temp == []:
            continue
        temp.sort(key=lambda item: item[1], reverse=True)
        
        max_num = temp[0][1]

        if max_num < 2:
            continue
        
        for i in temp:
            if i[1] == max_num:
                result.append(''.join(list(i[0])))

    answer = sorted(result)

    return answer
#%%
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))