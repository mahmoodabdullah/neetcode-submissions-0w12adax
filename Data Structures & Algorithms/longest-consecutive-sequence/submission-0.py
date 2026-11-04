class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        current_streak = 1

        if not nums:
            return 0

        nums.sort()

        for i in range(len(nums) - 1):
            current_num = nums[i]
            next_num = nums[i + 1]
            if current_num == next_num:
                continue
            if current_num + 1 == next_num:
                current_streak += 1
                longest = max(longest, current_streak)
            else:
                current_streak = 1

        return longest
            
            
        