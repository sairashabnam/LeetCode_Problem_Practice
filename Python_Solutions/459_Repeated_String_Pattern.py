class Solution:
#Solution1:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n//2 + 1):
            if n % i == 0:
                substring = s[:i]
                if substring * (n // i) == s:
                    return True
        return False
    

s = Solution()
# Example usage:
print(s.repeatedSubstringPattern("abcabcabc"))  # Output: True
print(s.repeatedSubstringPattern("abab"))       # Output: True
print(s.repeatedSubstringPattern("abcdeabcd"))   # Output: False
print(s.repeatedSubstringPattern("aaaaa"))      # Output: True