class Solution(object):
    def __init__(self) -> None:
        lst = []

        n = int(input("Enter number of elements : "))

        for i in range(0, n):
            ele = int(input())

            lst.append(ele)  # adding the element

        x = input("target = ")
        x = int(x)
        self.twoSum(lst, x)

    def twoSum(self, nums, target):
        res = {}

        for i in range(len(nums)):

            if res.get(nums[i]) != None:

                print([res.get(nums[i]), i])
                return [res.get(nums[i]), i]

            else:

                res[target - nums[i]] = i


Solution()
