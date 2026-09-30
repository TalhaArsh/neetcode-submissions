class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1 , max(piles)
        result = r

        while l <= r:
            midpoint = (l + r) // 2
            timeCount = 0 
            for b in piles:
                timeCount += math.ceil(b/midpoint)

            if timeCount > h:
                l = midpoint + 1
            else:
                r = midpoint - 1
                result = min(result,midpoint)

        return result


        

        
        