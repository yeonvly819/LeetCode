#%%
dial_dict = {'1':(0, 0), '2':(0, 1), '3':(0, 2),
             '4':(1, 0), '5':(1, 1), '6':(1, 2),
             '7':(2, 0), '8':(2, 1), '9':(2, 2),
             '*':(3, 0), '0':(3, 1), '#':(3, 2)}

k = 3
dial_dict[str(k)][0]
# %%
def solution(numbers, hand):
    answer = ''

    dial_dict = {'1':(0, 0), '2':(0, 1), '3':(0, 2),
                 '4':(1, 0), '5':(1, 1), '6':(1, 2),
                 '7':(2, 0), '8':(2, 1), '9':(2, 2),
                 '*':(3, 0), '0':(3, 1), '#':(3, 2)}

    left = ['1', '4', '7']
    right = ['3', '6', '9']
    middle = ['2', '5', '8', '0']
    
    left_cur = '*'
    right_cur = '#'
    
    for i in numbers:
        if str(i) in left:
            left_cur = str(i)
            answer += 'L'
        elif str(i) in right:
            right_cur = str(i)
            answer += 'R'
        else:
            left_distance = abs(dial_dict[str(i)][0] - dial_dict[left_cur][0]) + abs(dial_dict[str(i)][1] - dial_dict[left_cur][1])
            right_distance = abs(dial_dict[str(i)][0] - dial_dict[right_cur][0]) + abs(dial_dict[str(i)][1] - dial_dict[right_cur][1])

            if left_distance < right_distance:
                left_cur = str(i)
                answer += 'L'
            elif left_distance > right_distance:
                right_cur = str(i)
                answer += 'R'
            else:
                if hand == 'left':
                    left_cur = str(i)
                    answer += 'L'
                else:
                    right_cur = str(i)
                    answer += 'R'
    return answer
#%%
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))