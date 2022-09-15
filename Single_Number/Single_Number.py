class Solution(object):
    def singleNumber(self, nums):
        res = {}
        for val in nums:
            if res.get(val) != None:
                del res[val]
            else:
                res[val] = 1

        return res.popitem()[0]


print(Solution().singleNumber([2, 2, 1]))
print(Solution().singleNumber([4, 1, 2, 1, 2]))
print(Solution().singleNumber([1]))
