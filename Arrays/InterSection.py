class Solution:
    """
    Truly awful, worst memory, 11% runtime better
    """
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:

        intersect = []
        if len(nums1) > len(nums2):
            nums2.sort()
            sorted = nums2
            unsort = nums1
        else:
            nums1.sort()
            sorted = nums1
            unsort = nums2

        state = False
        for num in unsort:
            #implement binary search
            if len(sorted)> 0:
                state = self.binary_search(sorted, 0, len(sorted)-1, num)
            if state:
                intersect.append(num)
                sorted.remove(num)
                state = False

        return intersect

    def binary_search(self, arr, lo, hi, x):
        mid = lo + int((hi -lo)/2)
        if  x == arr[mid]:
            return True
        else:
            if mid in [lo, hi]:
                if x in [arr[lo], arr[hi]]:
                    return True
                else:
                    return False
            elif arr[mid] > x:
                return self.binary_search(arr, lo, mid, x)
            else:
                return self.binary_search(arr, mid, hi, x)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
nums3 = [1,2,2,1]
nums4 = [2,2]
print(Solution().intersect(nums1, nums2))

