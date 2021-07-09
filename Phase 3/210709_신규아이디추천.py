#%%
def solution(new_id):

    new_id = new_id.lower() # step1
    new_id = ''.join(re.compile('[a-z0-9-_.]?').findall(new_id)) # step2
    new_id = new_id.replace('...', '.') # step3
    new_id = new_id.replace('..', '.') # step3
    new_id = new_id.strip('.') # step4
    
    # step5
    if new_id == '':
        new_id += 'a'
    else:
        pass

    # step6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id.rstrip('.')

    # step7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    answer = new_id
    return answer
#%%
print(solution("z-+.^."))