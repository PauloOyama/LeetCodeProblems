class Solution(object):
    def __init__(self) -> None:
        x = input("s = ")
        self.isValid(x)

    def isValid(self, s):

        lst = []
        for i in range(len(s)):
            if s[i] == "{" or s[i] == "[" or s[i] == "(":
                lst.append(s[i])
            else:

                if not lst:
                    return False

                last = lst.pop()

                if last == "{" and s[i] == "}":
                    continue
                if last == "(" and s[i] == ")":
                    continue
                if last == "[" and s[i] == "]":
                    continue
                else:
                    return False

        if lst:
            return False
        else:
            return True


Solution()
