class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for i in range (2):
            for char in nums:
                res.append(char)

        return res
                
        