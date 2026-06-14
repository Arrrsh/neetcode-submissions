class Solution:
    def findMin(self, nums: List[int]) -> int:
        found_index = -1
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] <= nums[n - 1]:
                found_index = m
                right = m - 1
            else:
                left = m + 1
        return nums[found_index]