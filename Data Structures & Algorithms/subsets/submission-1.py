class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def explore(index):
            if index == len(nums):
                result.append(path.copy())
                return

            path.append(nums[index])
            explore(index+1)

            path.pop()

            explore(index+1)

        explore(0)
        return result
        