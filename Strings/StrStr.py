class Solution:
    """
    70% runtime
    50% memory
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for idx in range(len(haystack)-len(needle)+1):
            for j in range(0,len(needle)):
                if haystack[idx+j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return idx
        return -1



haystack = "hello"
needle = "ll"
haystack_2 = "aaaaa"
needle_2 = "bba"
haystack_3 = ""
needle_3 = ""
haystack_4 = ""
needle_4 = "a"
haystack_5 = "a"
needle_5 = "a"
print(Solution().strStr(haystack_5,needle_5))
