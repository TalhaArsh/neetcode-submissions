class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sort = {}

        for char in s:
            sort[char] = sort.get(char,0) + 1

        for char in t:
            if char not in sort or sort[char] == 0:
                return False
            sort[char] += -1

        
        return True
        