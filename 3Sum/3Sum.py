class Solution(object):
    def threeSum(self, nums):
        res = []
        for i in range(len(nums)):
            res.append(self.threeSum_(nums, []))

    def threeSum_(self, nums, lst):
        if len(lst) > 3:
            return []

        elif len(lst) == 3:

            sum = 0
            for i in lst:
                sum += i

            if sum == 0:
                return lst
            else:
                return []

        else:
            res = []
            for i in range(len(nums)):
                res.append(self.threeSum_(nums[(i+1):], lst + [nums[i]]))
            return res


Solution().threeSum([-1, 0, 1, 2, -1, -4])
