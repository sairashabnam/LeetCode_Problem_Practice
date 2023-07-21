class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Solution1:
        # s_list = [s[i] for i in range(0,len(s))]
        # s_list.sort()
        # t_list = [t[i] for i in range(0,len(t))]
        # t_list.sort()
        # if s_list == t_list:
        #     return True
        # else:
        #     return False
    #Solution2:
    # the sorted strings are checked
        if(sorted(s)== sorted(t)):
            return True
        else:
            return False
        

s = Solution()
# Another example with phrases:
phrase1 = "Astronomer"
phrase2 = "Moon starer"
if s.isAnagram(phrase1, phrase2):
    print(f"{phrase1} and {phrase2} are anagrams.")
else:
    print(f"{phrase1} and {phrase2} are not anagrams.")        