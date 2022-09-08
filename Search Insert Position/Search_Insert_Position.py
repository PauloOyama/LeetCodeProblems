class Solution(object):
    def searchInsert(self, nums, target):
        return self.searchInsert_(nums, target, 0)

    def searchInsert_(self, nums, target, idx):
        if len(nums) == 0:
            return idx

        if len(nums) == 1:
            if nums[0] == target or target < nums[0]:
                return idx
            else:
                return idx+1

        if len(nums) == 2:
            if nums[0] == target:
                return idx
            elif nums[1] == target:
                return idx+1
            elif target < nums[0]:
                return idx
            elif target > nums[1]:
                return idx+2
            else:
                return idx+1

        mid = len(nums) // 2

        if target <= nums[mid]:
            return self.searchInsert_(nums[0:mid], target, idx)
        else:
            return self.searchInsert_(nums[mid:], target, idx+mid)


print(Solution().searchInsert([1, 3, 4, 6], 5))
