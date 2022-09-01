class Solution(object):

    def __init__(self) -> None:
        s = input("s = ")
        t = input("t = ")
        self.isAnagram(s, t)

    def isAnagram(self, s, t):
        dic_s = {}
        dic_t = {}
        for i in s:
            if dic_s.get(i) == None:
                dic_s[i] = 1
            else:
                dic_s[i] += 1

        for i in t:
            if dic_t.get(i) == None:
                dic_t[i] = 1
            else:
                dic_t[i] += 1

        print(dic_t == dic_s)
        return True if dic_t == dic_s else False


Solution()
