#%%
class Solution:
    def singleNumber(self, nums) -> int:

        cnt_list = [0 * i for i in range(max(nums) + 1)]

        for i in nums:
            cnt_list[i] += 1

        for j in cnt_list:
            if j == 1:
                return cnt_list.index(j)

result = Solution()
print(result.singleNumber([4, 1, 2, 1, 2]))