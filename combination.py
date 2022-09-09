class Solution(object):
    def getConcatenation(self, nums):
        return nums + nums[::]


print(Solution().getConcatenation([1, 2, 1]))
