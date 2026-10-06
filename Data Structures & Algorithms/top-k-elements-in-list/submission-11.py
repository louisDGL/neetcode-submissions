class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for elt in nums:
            count[elt] = count.get(elt, 0) + 1

        heap = []
        for num, nb in count.items():
            heapq.heappush(heap, (nb, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append (heapq.heappop(heap)[1])
        return res