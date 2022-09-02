from curses.ascii import isalnum


class Solution(object):
    def __init__(self) -> None:
        s = input("s = ")
        self.isPalindrome(s)

    def isPalindrome(self, s: str):
        res = ""

        for i in s:
            if i.isalnum():
                res += i.lower()

        return res == res[::-1]


Solution()
