class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for x in strs:
            sortedX = ''.join(sorted(x))
            anagrams[sortedX].append(x)
        return list(anagrams.values())