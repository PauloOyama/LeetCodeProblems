class Solution(object):
    def containsDuplicate(self, nums):
        res = {}
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1

        for k, v in res.items():
            if v > 1:
                return True

        return False


print(Solution().containsDuplicate([1, 2, 3, 1]))
print(Solution().containsDuplicate([1, 2, 3, 4]))
print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
