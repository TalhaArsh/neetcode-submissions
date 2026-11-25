class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hasmap = defaultdict(int)
        hasmap2 = defaultdict(int)
        for character in s:
            hasmap[character] += 1
        for character in t:
            hasmap2[character] += 1

        if hasmap == hasmap2:
            return True
        return False