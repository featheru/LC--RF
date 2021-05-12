class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for idx in range(len(nums)-1):
            if nums[idx] == nums[idx+1]:
                return True
        return False



nums_1 = [0,4,5,0,3,6]
nums_2 = [1,1,1,3,3,4,3,2,4,2]
nums_3 = [1,2,3,4]
print(Solution().containsDuplicate(nums_2))