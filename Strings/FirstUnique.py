class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return
        -1.
        memory: 67%
        runtime: 9%
        """
        length = len(s)
        # sort through current letters
        for idx in range(length):
            # sort through letters after current letter to find no repetition
            state = False
            for idx_2 in range(0,length):
                if idx_2 != idx:
                    if s[idx] == s[idx_2]:
                        state = True
                        break
            if not state:
                return idx

        return -1



s = "leetcode"
s_2 = "loveleetcode"
s_3 = "cc"
print(Solution().firstUniqChar_2(s_2))




