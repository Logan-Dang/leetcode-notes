class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        res = ''
        for i in range(len(s)):
            if i + 1 >= len(s): continue
            if i > 0 and s[i - 1] == s[i + 1]:
                left, right = i - 1, i + 1
                mini_res = s[i]
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    mini_res = s[left] + mini_res + s[right]
                    left -= 1
                    right += 1
                if len(mini_res) > len(res):
                    res = mini_res
            if s[i] == s[i + 1]:
                left, right = i, i + 1
                mini_res = ''
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    mini_res = s[left] + mini_res + s[right]
                    left -= 1
                    right += 1
                if len(mini_res) > len(res):
                    res = mini_res
            mini_res = s[i]
            if len(mini_res) > len(res):
                    res = mini_res
        return res
