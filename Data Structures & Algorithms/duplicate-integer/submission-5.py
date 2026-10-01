class Solution:
    def hasDuplicate(self,num):
        return len(num) != len(set(num))
s1 = Solution()
s1.hasDuplicate([1,2,3,3])