class Solution(object):
    def removeStars(self, s):
        new_string = []
        for char in list(s):
            if char == '*':
                new_string.pop()
            else:
                new_string.append(char)
        return ''.join(new_string)
    
s = "leet**cod*e"
sol = Solution()
print(sol.removeStars(s))