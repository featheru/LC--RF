class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        runtime: 61%
        memory: 82%
        """
        idx = 0
        idx_2 = len(s)-1
        while idx < idx_2:
            if not s[idx].isalnum():
                idx += 1
            elif not s[idx_2].isalnum():
                idx_2 -= 1
            elif s[idx].lower() == s[idx_2].lower():
                idx += 1
                idx_2 -= 1
            else:
                return False

        return True

s = "A man, a plan, a canal: Panama"
s_2 = "race a car"
s_3 = "ab@a"
print(Solution().isPalindrome(s_3))
