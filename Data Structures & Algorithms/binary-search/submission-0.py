class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begIndex = 0
        endIndex = len(nums) - 1

        while begIndex <= endIndex:
            midValue = nums[(begIndex + endIndex) // 2]

            if midValue == target:
                return (begIndex + endIndex) // 2
            
            elif midValue > target:
                endIndex = ((begIndex + endIndex) // 2) - 1

            else:
                begIndex = ((begIndex + endIndex) // 2) + 1

        return -1
        