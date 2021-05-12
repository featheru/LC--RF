class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        idx = -1
        while abs(idx) <= len(digits):
            if digits[idx] < 9:
                digits[idx] += 1
                return digits
            else:
                digits[idx] = 0
                if abs(idx-1) > len(digits):
                    #add index value to front
                    digits.insert(0,1)
                    return digits
                else:
                    idx -= 1

# TESTING
digits = [1, 2, 3]
Solution().plusOne(digits)
print(digits)