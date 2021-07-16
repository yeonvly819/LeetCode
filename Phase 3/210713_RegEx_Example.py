#%%
import re
# 1. 핸드폰 번호 010/011/017/016-0000-0000

pattern = '[(010)(011)(016)(017)]+-[1-9][0-9]{3}-[1-9][0-9]{3}'

test_string1 = '010-0000-0000'
test_string2 = '017-1000-8989'

print(re.compile(pattern).findall(test_string1))
print(re.compile(pattern).findall(test_string2))
# %%
pattern = '[(010)(011)(016)(017)]'

test_string1 = '010'
print(re.compile(pattern).findall(test_string1))