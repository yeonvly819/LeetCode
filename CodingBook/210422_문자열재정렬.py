# 입력된 문자열에서 문자와 숫자를 구분한 후 문자는 오름차순 정렬하고 숫자는 더해서 합침

S = input()

w = ''
n = 0

for i in S:
    try:
        if int(i):
            n += int(i)
    except:
        w += i

w = ''.join(sorted(list(w), reverse=False))

print(w + str(n))
