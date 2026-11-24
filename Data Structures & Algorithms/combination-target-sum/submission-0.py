class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def explore(index,remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            if remaining <0:
                return
            if index == len(nums):
                return

            path.append(nums[index])
            explore(index,remaining - nums[index])

            path.pop()

            explore(index+1,remaining)

        explore(0,target)
        return result