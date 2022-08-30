class Solution(object):

    def __init__(self) -> None:
        lst = []

        n = int(input("Enter number of elements : "))

        for i in range(0, n):

            lst.append(input())  # adding the element

        self.longestCommonPrefix(lst)

    def longestCommonPrefix(self, strs):

        if not strs:
            return ""

        count = 0

        for i in range(len(strs[0])):

            character = strs[0][i]

            aux = 0

            for j in range(len(strs)):

                if i == len(strs[j]):
                    return strs[0][:count]

                if character == strs[j][i]:
                    aux += 1

            if aux == len(strs):
                count += 1
            else:
                break

        return strs[0][:count]


Solution()
