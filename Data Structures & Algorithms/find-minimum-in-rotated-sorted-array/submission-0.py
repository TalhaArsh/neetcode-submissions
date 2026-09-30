class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1

        while (l < r):
            midPoint = (l+r)//2
            midValue = nums[midPoint]

            if midValue > nums[r]:
                l = midPoint + 1
        
            elif midValue < nums[r]:
                r = midPoint

        return nums[l]


        