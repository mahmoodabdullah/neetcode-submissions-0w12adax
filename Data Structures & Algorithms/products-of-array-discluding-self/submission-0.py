class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_answer = []

        for index_to_remove in range(len(nums)):
            result = 1

            new_list = nums[:index_to_remove] + nums[index_to_remove + 1:]
            
            for i in new_list:
                result *= i

            final_answer.append(result)

        return final_answer
        