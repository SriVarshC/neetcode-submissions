class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1

        n = len(nums)

        bucket = [[] for _  in range(n+1)]

        for i in freq:
            bucket[freq[i]].append(i)

        answer = []

        for i in range(n,0,-1):
            for j in bucket[i]:
                answer.append(j)

                if len(answer) == k:
                    return answer
