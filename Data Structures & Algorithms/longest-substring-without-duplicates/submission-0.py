class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        last_seen = {}

        for i in range(len(s)):
            if s[i] in last_seen:
                left = max(left,last_seen[s[i]]+1)
            last_seen[s[i]] = i
            max_length = max(max_length, i - left +1)
        return max_length
