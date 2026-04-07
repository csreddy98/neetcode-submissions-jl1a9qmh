class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))
            output[sorted_str].append(s)
        return output.values()