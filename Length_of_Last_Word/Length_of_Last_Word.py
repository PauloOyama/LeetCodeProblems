class Solution(object):
    def lengthOfLastWord(self, s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        index = len(s) - 1
        i = 0

        while (index > 0) and not (s[index-1] == ' ' and s[index] != ' '):
            if s[index] == ' ':
                i += 1
            index -= 1

        res = s[(index): (len(s) - i)]

        return len(res)


print(Solution().lengthOfLastWord("Hello World"))
print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
print(Solution().lengthOfLastWord("luffy is still joyboy"))
print(Solution().lengthOfLastWord("day"))
print(Solution().lengthOfLastWord("a "))
