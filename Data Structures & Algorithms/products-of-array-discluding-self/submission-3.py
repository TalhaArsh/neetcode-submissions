class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        runningprefix = 1

        for i in range(1,len(nums)):
            runningprefix *= nums[i -1]
            res[i] = runningprefix

        runningpostfix = 1

        for i in range(len(nums)-2,-1,-1 ):
            runningpostfix *= nums[i + 1]
            res[i] *= runningpostfix

        return res



# -1 0 1 2 3 
#  1 -1 0 0 0
#           0