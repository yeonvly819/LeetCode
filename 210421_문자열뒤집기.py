# 중복된 값을 하나의 값으로 바꾸기
# 전체 문자열 길이와 int로 변환 후 합(= 1의 개수)을 비교 후 더 적은 수를 택함

nums = input()

new_num = nums[0]

for i in nums:
    if new_num[-1] == i:
        pass
    else:
        new_num += i

print(min(len(new_num), sum(map(int, list(new_num)))))
