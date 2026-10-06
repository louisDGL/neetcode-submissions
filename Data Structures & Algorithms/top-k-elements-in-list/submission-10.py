class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for elt in nums:
            count[elt] = count.get(elt, 0) + 1
        for elt, cnt in count.items():
            freq[cnt].append(elt)
        
        final = []
        for i in range (len(freq) - 1, 0, -1):
            for num in freq[i]:
                final.append(num)
                if len(final) >= k:
                    return final
