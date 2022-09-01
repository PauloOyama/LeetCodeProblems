class Solution(object):

    def __init__(self) -> None:
        x = input("length = ")
        lst = []
        for i in range(int(x)):
            lst.append(int(input()))

        self.removeDuplicates(lst)

    def removeDuplicates(self, nums):
        l = 0
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                nums[l+1] = nums[r]
                l += 1
        return l+1


Solution()
