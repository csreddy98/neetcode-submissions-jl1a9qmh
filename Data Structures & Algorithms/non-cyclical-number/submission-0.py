class Solution:
    def isHappy(self, n: int) -> bool:
        curr = str(n)
        seen = set()
        while curr != 1:
            x = 0
            for i in curr:
                x += int(i) ** 2
            if x == 1:
                break
            elif x in seen:
                return False
            else:
                seen.add(x)
                curr = str(x)
        return True