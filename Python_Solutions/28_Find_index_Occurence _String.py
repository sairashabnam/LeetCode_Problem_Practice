class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    

s = Solution()

haystack = "sadbutsad"
needle = "sad"

print(s.strStr(haystack, needle))

haystack = "leetcode"
needle = "leeto"
print(s.strStr(haystack, needle))