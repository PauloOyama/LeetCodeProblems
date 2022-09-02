from turtle import right


class Solution(object):
    def __init__(self) -> None:
        x = input("length = ")
        lst = []
        for i in range(int(x)):
            lst.append(int(input()))
        target = int(input("target = "))
        self.searchInsert(lst, target)

    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return 0 if nums[0] > target else 1

        aux = nums
        index = 0
        while True:

            if len(aux) == 2:
                break

            half = len(aux)//2
            left = aux[:half]
            right = aux[half:]

            if target >= right[0]:
                index += len(left)
                aux = right

            elif target <= left[(half - 1)]:
                aux = left
            else:
                return (index + len(left))

        if nums[index] == target:
            return index
        else:
            print(index if nums[index] > target else (index + 1))
            return (index) if nums[index] > target else (index + 1)


Solution()
