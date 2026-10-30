class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        max_area = 0

        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                popped_index = stack.pop()
                height = heights[popped_index]

                right = i

                if stack:
                    left = stack[-1]
                else:
                    left = -1
                
                width = right - left - 1

                current_area = height*width

                max_area = max(max_area,current_area)

            stack.append(i)
        return max_area
        