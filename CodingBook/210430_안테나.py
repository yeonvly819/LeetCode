N = int(input())
location = list(map(int, input().split()))

location.sort()

if len(location) % 2 == 0: # 길이가 짝수일 경우
    median_idx = len(location) // 2 - 1
else: # 길이가 홀수일 경우
    median_idx = len(location) // 2
    
print(location[median_idx])
