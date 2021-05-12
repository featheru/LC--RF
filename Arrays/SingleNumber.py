class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """86% percentile for memory, 7% for runtime"""
        for idx in range(len(nums)):
            curr_num = nums[idx]
            if curr_num not in nums[idx+1:] and curr_num not in nums[:idx]:
                return curr_num

    def singleNumber_listmod(self, nums: list[int]) -> int:
        """????"""
        idx = 0
        while idx != len(nums):
            curr_num = nums[idx]
            if curr_num not in nums[idx+1:]:
                return curr_num
            else:
                nums.remove(curr_num)
                nums.remove(curr_num)


list_1 = [1,2,1,2,4]
print(Solution().singleNumber_listmod(list_1))