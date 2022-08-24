class Solution(object):

    def __init__(self) -> None:
        x = input("s = ")
        self.romanToInt(x)

    def romanToInt(self, x):

        roman = {
            "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1
        }

        x = x.replace("\"", "")

        result = 0
        for i in range(len(x)):

            if ((i + 1) != len(x)) and (roman[x[i]] < roman[x[i+1]]):
                result -= roman[x[i]]
            else:
                result += roman[x[i]]

        return result


Solution()
