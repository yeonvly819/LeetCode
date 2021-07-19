#%%
def solution(n, lost, reserve):
    
    peclass = []

    for i in reserve:
        if i in lost:
            peclass.append(i)
    
    for i in peclass:
        if i in reserve:
            reserve.remove(i)
        if i in lost:
            lost.remove(i)
            
    for i in reserve:
        if (i-1) in lost:
            peclass.append(i)
            peclass.append(i-1)
            lost.remove(i-1)

        elif (i+1) in lost:
            peclass.append(i)
            peclass.append(i+1)
            lost.remove(i+1)

        elif i not in peclass:
            peclass.append(i)

    for i in range(1, n+1):
        if i in lost:
            pass
        elif i not in peclass:
            peclass.append(i)

    answer = len(peclass)
    return answer
#%%
# print(solution(5, [2, 4], [1, 3, 5]))
# print(solution(5, [2, 4], [3]))
# print(solution(3, [3], [1]))
print(solution(5, [1, 2, 3], [2, 3, 4]))
#%%
# 맹한쓰앵님
def solution(n, lost, reserve):
    answer = n - len(lost) # 3명
    res = []
    # 여벌 체육복을 가져온 학생이 도난당한 경우
    for r in reserve:
        if r in lost:
            lost.remove(r)
            answer += 1
        else:
            res.append(r)
    # 앞뒤
    for r in res:
        if (r-1) in lost:
            lost.remove(r-1)
            answer += 1
        elif (r+1) in lost:
            lost.remove(r+1)
            answer += 1
            
    return answer