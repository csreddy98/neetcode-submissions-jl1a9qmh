class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = re.sub(r'[^a-zA-Z0-9\s]', '', s).replace(' ', '').lower()
        print(cleanS)
        if cleanS == cleanS[::-1]:
            return True
        return False