class Solution(object):

    def __init__(self) -> None:
        x = input("s = ")
        self.isPalindrome(int(x))

    def isPalindrome(self, x):

        aux = x
        reverse = 0
        while aux > 0:
            last = aux % 10
            reverse = reverse*10 + last
            aux = aux // 10

        return True if x == reverse else False


Solution()
