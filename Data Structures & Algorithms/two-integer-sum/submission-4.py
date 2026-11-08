class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            need = target - num
            if num in seen:
                return [seen[num],i]
            seen[need] = i
       

        