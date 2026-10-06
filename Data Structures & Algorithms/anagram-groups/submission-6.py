class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for elt in strs:
            sortedS = ''.join(sorted(elt))
            res[sortedS].append(elt)
        return list(res.values())