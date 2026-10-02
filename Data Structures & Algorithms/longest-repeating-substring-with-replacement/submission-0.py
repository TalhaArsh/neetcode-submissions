class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxLength = 0
        charFrq = {}
    
        for r in range(len(s)):
            if s[r] not in charFrq:
                charFrq[s[r]] = 0
            charFrq[s[r]] += 1

            while (r - l + 1) - max(charFrq.values() ) > k:
                charFrq[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r- l + 1)

        return maxLength


        