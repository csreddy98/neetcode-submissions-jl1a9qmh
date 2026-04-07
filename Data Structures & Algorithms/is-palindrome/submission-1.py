class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        new_s = re.sub('[^A-Za-z]+', '', s).lower()
        print(new_s)
        count = len(new_s)
        for i in range(len(s) // 2):
            if new_s[i] != new_s[(i + 1) * -1]:
                return False
        return True