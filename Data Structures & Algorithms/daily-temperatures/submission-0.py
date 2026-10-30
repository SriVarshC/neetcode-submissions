class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                previous_idx = stack[-1]
                answer[previous_idx] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return answer