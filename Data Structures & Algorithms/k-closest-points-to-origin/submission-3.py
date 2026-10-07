class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for point in points:
            heapq.heappush(distances, [-((point[0])**2 + (point[1])**2), point[0], point[1]])
            if len(distances) > k:
                heapq.heappop(distances)

        return [[vect[1], vect[2]] for vect in distances]
