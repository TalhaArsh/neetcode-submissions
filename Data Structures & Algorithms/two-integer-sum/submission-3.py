class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevValue = defaultdict(int)

        for i, n in enumerate(nums):
            prev = target - n
            if prev in prevValue:
                return [prevValue[prev],i]
            prevValue[n] = i