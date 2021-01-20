class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        i1 = 0
        i2 = 0
        mylen = len(nums)
        while i2 < mylen:
            while i2 < mylen and nums[i2] == nums[i1]:
                i2 += 1
            if i2 < mylen and nums[i2] != nums[i1]:
                i1 += 1
                nums[i1] = nums[i2]
        return i1 + 1