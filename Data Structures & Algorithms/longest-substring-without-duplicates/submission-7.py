class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = []
        res = 0
        for si in s:
            if si not in track:
                track.append(si)
                res = max(res, len(track))
            else:
                while si in track:
                    track.pop(0)
                track.append(si)
        return res