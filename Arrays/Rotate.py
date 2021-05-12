
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        kmod = k % length

        if kmod == 0:
            return

        visited_list = set()
        idx_start = 0
        idx = 0
        val_swap = nums[idx]

        while len(visited_list) < length:
            idx = (idx + kmod) % length
            if idx in visited_list:
                idx_start += 1
                idx = idx_start
                val_swap = nums[idx]
            else:
                visited_list.add(idx)
                tmp = nums[idx]
                nums[idx] = val_swap
                val_swap = tmp

#TESTING

list_1 = [0,1,2,3,4,5,6,7]
k_1 = 4
Solution().rotate(list_1, k_1)
print(list_1)