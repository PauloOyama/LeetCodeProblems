class Solution(object):

    def __init__(self) -> None:
        x = input("ransomNote  = ")
        y = input("magazine  = ")
        self.canConstruct(x, y)

    def canConstruct(self, ransomNote, magazine):

        count = 0
        aux = ransomNote
        for i in magazine:
            for j in range(len(aux)):
                if i == aux[j]:
                    count += 1
                    aux = aux[:j] + "" + aux[j+1:]
                    break
            if count == len(ransomNote):
                return True

        return False


Solution()
