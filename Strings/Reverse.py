class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        runtime = 78%
        memory = 19%
        change length
        runtime = 63%
        memory = 81%
        """
        length = int(len(s)/2)
        for i in range(length):
            s[i], s[-i - 1] = s[-i-1], s[i]
        return

s = ["h","e","l","l"]
Solution().reverseString(s)
print(s)


