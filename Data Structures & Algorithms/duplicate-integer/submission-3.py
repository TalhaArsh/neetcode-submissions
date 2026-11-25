class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict()

        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = 1
        
        return False