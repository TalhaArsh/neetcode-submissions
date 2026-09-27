class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for c in nums:
            count[c] += 1
        
        freq = sorted(count,key = count.get,reverse= 'True')
        

        print(freq)

        return freq[:k]

        
        