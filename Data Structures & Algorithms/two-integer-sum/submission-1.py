class Solution:
    def twoSum(self, nums, target: int):
        dict={}
        for i in range(0,len(nums)):
            cur = nums[i]
            req = target - cur
            if req in dict:
                return [dict[req],i]
            dict[cur]=i


s = Solution()
s.twoSum([3,4,5,6],7)
            

