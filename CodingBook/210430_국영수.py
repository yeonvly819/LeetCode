import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
sys.stdin.readline()

name_score = []

for _ in range(N):
    data = list(sys.stdin.readline().replace('\n', '').split())
    name_score.append([data[0], int(data[1]), int(data[2]), int(data[3])]) # 이름은 str 그대로, 점수는 int로 변환

result = sorted(name_score, key=lambda x: (-x[1], x[2], -x[3], x[0])) # 비교할 아이템의 요소가 복수 개인 경우, 튜플로 그 순서를 보내줌; -를 붙이면 내림차순 정렬

for i in result:
    print(i[0])
