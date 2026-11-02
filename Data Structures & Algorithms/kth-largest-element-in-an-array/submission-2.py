class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        left = 0
        right = len(nums) - 1

        while left <= right:

            pivot = nums[right]
            store_index = left

            for i in range(left,right):
                if nums[i]<=pivot:
                    nums[store_index],nums[i] = nums[i],nums[store_index]
                    store_index += 1

            nums[store_index],nums[right] = nums[right],nums[store_index]

            pivot_index = store_index

            if pivot_index == target:
                return nums[pivot_index]

            elif pivot_index < target:
                left = pivot_index + 1

            else:
                right = pivot_index - 1




