from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []
        dq = deque()

        for right in range(len(nums)):
            left = right - k + 1

            while dq and dq[0] < left:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)

            if right >=k - 1:
                result.append(nums[dq[0]])
        return result
        
        