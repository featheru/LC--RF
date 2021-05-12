class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        23.57% of runtime
        88% of memory
        """
        zero = 0
        idx = 0
        length = len(nums)
        while idx != length - 1 - zero:
            if not nums[idx]:
                #remove zero and add to end
                nums.remove(0)
                zero += 1
                nums.append(0)
            else:
                idx += 1


nums = [0,1,0,3,0,12,0]
nums_2 = [0,0,1]
Solution().moveZeroes(nums_2)
print(nums_2)


