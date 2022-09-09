class Solution(object):
    def plusOne(self, digits):
        index = len(digits) - 1
        carry_one = False

        while index >= 0:
            if digits[index] == 9:
                digits[index] = 0
                carry_one = True
                index -= 1
            else:
                digits[index] += 1
                if carry_one:
                    carry_one = not carry_one
                break

        if carry_one:
            digits = [1] + digits

        return digits


print(Solution().plusOne([1, 2, 3]))
print(Solution().plusOne([4, 3, 2, 1]))
print(Solution().plusOne([8, 9, 9, 9]))
