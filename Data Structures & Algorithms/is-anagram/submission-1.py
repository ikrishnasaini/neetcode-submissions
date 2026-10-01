class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        for ele in s:
            if ele not in dict:
                dict[ele]=1
            else:
                dict[ele]+=1
        for ele in t:
            if ele not in dict or dict[ele]==0:
                return False
            else:
                dict[ele]-=1
        return True

s = Solution()
s.isAnagram("racenar","carrace")
        