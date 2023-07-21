class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_str = ""
        for i in range(0,max(len(word1), len(word2))):
            if(i < len(word1)):
                merge_str += word1[i]
            if(i < len(word2)):
                merge_str += word2[i]
        return merge_str
    


s = Solution()

word1 = "abc"
word2 = "pqr"

print(s.mergeAlternately(word1, word2))