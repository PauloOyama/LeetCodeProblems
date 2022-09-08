class Solution(object):
    def __init__(self) -> None:
        x = input("length = ")
        lst = []
        for i in range(int(x)):
            lst.append(int(input()))

        target = input("val = ")
        target = int(target)
        self.removeElement(lst, target)

    def removeElement(self, nums, val):
        l = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        return l


Solution()
