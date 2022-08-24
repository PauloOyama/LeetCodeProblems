class Solution(object):

    def __init__(self) -> None:
        x = input("s = ")
        self.isPowerOfFour(x)

    def isPowerOfFour(self, n):
        n = int(n)

        while (n % 4 == 0):
            n = n/4

        if n == 1:
            return True

        if n % 2 != 0:
            return False


Solution()
