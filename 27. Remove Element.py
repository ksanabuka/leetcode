import sys

# if val found - swap to the end count from end and back 

class Solution:

    # 1034
    # 1304
    # 1340
    def moveToEnd(self, nums: [int], valInd: int, endInd: int):
        while valInd < endInd:
            tmp = nums[valInd]
            nums[valInd] = nums[valInd + 1]
            nums[valInd + 1] = tmp
            valInd += 1

           
    def removeElement(self, nums: [int], val: int) -> int:
        endInd = len(nums) - 1
        startInd = 0
        while val in nums[startInd:endInd]: 
            startInd = nums.index(val)
            self.moveToEnd(nums, startInd, endInd)
            endInd -= 1

        if val in nums:
            return nums.index(val)
        else:
            return len(nums)


nums = [1,0,0,4]
val = 0
a = Solution()
a.removeElement(nums, val)
# print(nums)
# a.moveToEnd(nums, 2, len(nums) - 1)    

print (nums)
