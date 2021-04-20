# 값이 0이나 1인 경우 더하기
# result가 0인 경우 해당 step의 숫자는 더하기

nums = list((map(str, input())))

result = 0

for i in nums:
    if (result == 0) | (int(i) == 1) | (int(i) == 0):
        result += int(i)

    else:
        result *= int(i)

print(result)
