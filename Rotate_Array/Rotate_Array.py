
# TODO = Incomplete
class Solution(object):
    def rotate(self, nums, k):
        if len(nums) == 0:
            return nums

        k = k % len(nums)

        cut = len(nums) - k
        return nums[cut:] + nums[:cut]
    # def rotate(self, nums, k):
    #     if len(nums) == 0:
    #         return nums

    #     k = k % len(nums)

    #     if k == 0:
    #         return nums

    #     while k > 0:
    #         last = nums[len(nums) - 1]
    #         index = len(nums) - 1
    #         while (index - 1) >= 0:
    #             nums[index] = nums[index-1]
    #             index -= 1

    #         nums[0] = last

    #         k -= 1

    #     return nums


print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(Solution().rotate([-1, -100, 3, 99], 2))
print(Solution().rotate([1], 1))
