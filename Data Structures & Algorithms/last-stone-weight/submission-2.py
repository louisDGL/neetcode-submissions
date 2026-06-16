class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones =  [-s for s in stones]
        heapq.heapify (stones)

        while len(stones) > 1 :
            max1 = -1 *  heapq.heappop(stones)
            max2 = -1 * heapq.heappop(stones)
            if max1 > max2:
                heapq.heappush(stones, -1 * (max1 - max2))
        
        stones.append(0)
        return abs(stones[0])