class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2

        if len(a)>len(b):
            a,b = b,a

        total = len(a) + len(b)
        left_size = (total + 1)//2

        left = 0
        right = len(a)

        while left <= right:
            i = (left + right)//2
            j = left_size - i

            aleft = a[i-1] if i>0 else float("-inf")
            aright = a[i] if i < len(a) else float("inf")

            bleft = b[j-1] if j>0 else float("-inf")
            bright = b[j] if j < len(b) else float("inf")

            if aleft <= bright and bleft <= aright:
                if total % 2 == 1:
                    return max(aleft,bleft)
                else:
                    return (max(aleft,bleft)+min(bright,aright))/2

            elif aleft > bright:
                right = i - 1
            else:
                left = i + 1