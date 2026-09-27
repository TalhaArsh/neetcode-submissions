class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
    
        for i in range (len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            currentValue = nums[i]
            l,r = i + 1, len(nums) - 1
            while l < r:
             
                intermSum = nums[l] + nums[r]

                if intermSum == (-1 * currentValue):
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

                elif intermSum < (-1 * currentValue):
                    l += 1
                else: 
                    r -= 1
        
        return result
        