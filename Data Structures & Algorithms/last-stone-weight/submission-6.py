class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]

        heapq.heapify (heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
        
            if x > y:
                y = x - y
                heapq.heappush(heap, -y)

        heap.append(0)
        return abs(heap[0])