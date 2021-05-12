class Solution:
    def myAtoi(self, s: str) -> int:
        """
        57% for memory
        57% for runtime
        """

        idx = 0
        val = 0
        sign = None
        while idx < len(s):
            if s[idx] == ' ' and sign == None and val == 0:
                pass
            elif s[idx] == '-' and sign == None:
                sign = -1
            elif s[idx] == '+' and sign == None:
                sign = 1
            elif s[idx] in "0123456789":
                if sign == None:
                    sign = 1
                val = val*10 + int(s[idx])
            else:
                break
            idx +=1

        if sign == -1:
            val = -1 * val

        MAX = 2**31-1
        MIN = -2**31
        if MIN <= val <= MAX:
            return val
        elif MIN > val:
            return MIN
        else:
            return MAX

val1 = "00000-42a1234"
val2 = "   +0 123"
print(Solution().myAtoi(val2))