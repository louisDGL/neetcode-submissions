class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        seen = set()

        for elt in strs:
            eltSorted = ''.join(sorted(elt))
            if eltSorted in seen:
                output[eltSorted].append(elt)
            else:
                seen.add (eltSorted)
                output [eltSorted] = [elt]
        return list(output.values())