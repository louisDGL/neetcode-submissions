class TimeMap:

    def __init__(self):
        self.timestamp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        valeurs = self.timestamp[key]

        left = 0
        right = len(valeurs) - 1

        while left <= right:
            middle = (left + right) // 2
            if valeurs[middle][0] == timestamp:
                return valeurs[middle][1]
            if (middle + 1 >= len(valeurs) or valeurs[middle + 1] [0] > timestamp) and valeurs[middle][0] < timestamp:
                return valeurs[middle][1]
            
            if valeurs[middle][0] > timestamp:
                right = middle - 1
            if valeurs[middle][0] < timestamp:
                left = middle + 1
        
        return ""