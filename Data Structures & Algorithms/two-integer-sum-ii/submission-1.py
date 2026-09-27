class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0 , len(numbers) - 1

        while l < r :
            
            tempSum = numbers[l] + numbers[r]
            
            if tempSum > target:
                r -= 1

            if tempSum  < target:
                l += 1
            
            if tempSum == target:
                return [l + 1,r + 1]

        return False 




        

        