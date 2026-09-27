class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for c in nums:
            count[c] = count.get(c, 0) + 1
        
        freq = sorted(count,key = count.get,reverse= 'True')
        

        print(freq)

        return freq[:k]

        
        