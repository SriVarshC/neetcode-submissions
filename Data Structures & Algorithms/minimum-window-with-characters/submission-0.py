class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = {}

        for ch in range(len(t)):
            need[t[ch]] = need.get(t[ch],0)+1

        window = {}
        left = 0
        have = 0
        required = len(need)

        result = [-1,-1]
        result_length = float("inf")

        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0)+1

            if s[right] in need and window[s[right]] == need[s[right]]:
                have +=1

            while have == required:
                if (right - left + 1) < result_length:
                    result = [left,right]
                    result_length = right - left + 1

                window[s[left]] -=1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -=1
                left +=1

        if result_length == float("inf"):
            return ""
        return s[result[0]:result[1]+1]