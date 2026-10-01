class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashMap = {}
        length = len(points)
        
        for i in range (length):
            distance = math.sqrt(points[i][0]**2 + points[i][1]**2)
            print(distance)
            if distance not in hashMap.keys():
                hashMap[distance] = []
            hashMap[distance].append([points[i][0],points[i][1]])

            hashMap = dict(sorted(hashMap.items()))
        sortedHash = sorted(hashMap.items())
        result = []

        for distance, points in sortedHash:
            for point in points:
                result.append(point)

                if len(result) == k:
                    return result

        