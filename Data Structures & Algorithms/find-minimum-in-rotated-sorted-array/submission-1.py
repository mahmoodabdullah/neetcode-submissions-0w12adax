class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if nums[i - 1] >= num:
                return num
            else:
                i += 1
        