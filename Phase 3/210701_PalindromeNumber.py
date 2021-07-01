class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            if str(x) == str(x)[::-1]:
                return True
            else:
                return False

result = Solution()
result.containsDuplicate(123)