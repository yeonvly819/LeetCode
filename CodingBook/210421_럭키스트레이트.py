# 입력되는 수가 무조건 짝수이므로 반으로 나눠 더해서 비교하기
# 입력이 int이므로 str으로 바꾸어 슬라이싱하고 다시 int로 바꾸는 작업이 

N = int(input())

half = int(len(str(N)) / 2)

if sum(map(int, str(N)[:half])) == sum(map(int, str(N)[half:])):
    print('LUCKY')
else:
    print('READY')
