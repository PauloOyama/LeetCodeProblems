class Solution(object):

    def __init__(self) -> None:
        x = input("length = ")
        lst = []
        for i in range(int(x)):
            lst.append(int(input()))

        self.removeDuplicates(lst)

    def removeDuplicates(self, nums):
        i = 0
        while i != len(nums):
            if (i+1) == len(nums):
                i += 1
                continue
            if nums[i] == nums[i+1]:
                if len(nums) == 2:
                    return 1
                j = i
                while (j+2) != len(nums):
                    aux = nums[j+1]
                    nums[j+1] = nums[j+2]
                    nums[j+2] = aux
                    j += 1
                i -= 1

            if nums[i] > nums[i+1]:
                return i+1

            i += 1

        return len(nums)


Solution()
# print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
