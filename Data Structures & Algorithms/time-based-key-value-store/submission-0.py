class TimeMap:

    def __init__(self):
        self.keyStore= {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore.keys():
            self.keyStore[key] = []

        self.keyStore[key].append([value,timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res,values = "", self.keyStore.get(key,[])
        l,r = 0, len(values) - 1
        while l <= r:
            midPoint = (l+r) // 2
            midVal = values[midPoint][1]
            if midVal <= timestamp:
                l=midPoint + 1
                res = values[midPoint][0]
            else:
                r = midPoint - 1
        return res

        
