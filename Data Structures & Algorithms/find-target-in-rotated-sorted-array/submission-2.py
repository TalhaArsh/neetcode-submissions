class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            midpoint = (l + r) // 2
            midValue = nums[midpoint]

            if midValue == target:
                return midpoint

            # Left half is sorted
            if nums[r] < midValue:
                if nums[l] <= target < midValue:
                    r = midpoint - 1
                else:
                    l = midpoint + 1

            # Right half is sorted
            else:
                if midValue < target <= nums[r]:
                    l = midpoint + 1
                else:
                    r = midpoint - 1

        return -1