class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_l = list(set(nums))
        
        unique_l.sort(key=nums.count, reverse=True)

        return unique_l[:k]
        

        