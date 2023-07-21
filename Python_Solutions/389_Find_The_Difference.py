class Solution:
    def find_the_difference(self, s: str, t: str) -> str:
    #solution1:
        # list_s = [s[i] for i in range(0, len(s))]
        # list_t = [t[i] for i in range(0, len(t))]
        # for elem in list_s:
        #     list_t.remove(elem)
        # return list_t[0]
    #solution2:
        c = 0
        for cs in s:
            c ^= ord(cs)  # ord is ASCII value "^=" does an XOR operation
        for ct in t:
            c ^= ord(ct)
        print(c)
        return chr(c)  # chr = convert ASCII into character



s = Solution()
t = s.find_the_difference("abcd", "abcde")
print(t)

se = ""
t = "y"

t = s.find_the_difference(se, t)
print(t)
