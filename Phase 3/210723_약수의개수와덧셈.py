#%%
def divisor_sign(n):
    cnt = 0

    for i in range(1, int(n**(1/2)) + 1):
        if n == i ** 2:
            cnt += 1
        elif n % i == 0:
            cnt += 2
    
    if cnt % 2 == 0:
        return True
    else:
        return False

def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        sign = divisor_sign(i)

        if sign == True:
            answer += i
        else:
            answer -= i

    return answer
#%%
print(solution(13, 17))
#%%
14 % 7