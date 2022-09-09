class Solution(object):
    def lengthOfLastWord(self, s):
        index = len(s) - 1
        i = 0
        validator = True

        while s[index] != ' ' or validator:
            if s[index] != ' ':
                validator = False
                i += 1

            index -= 1

        return i


print(Solution().lengthOfLastWord("Hello World"))
print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
print(Solution().lengthOfLastWord("luffy is still joyboy"))
