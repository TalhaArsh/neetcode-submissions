class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair:pair[0])
        output = []
        output.append(intervals[0])
        
        for startVal, endVal in intervals[1:]:
            lastEndPoint = output[-1][1]
            if startVal <= lastEndPoint:
                #replace value instead of add
                output[-1][1] = max(lastEndPoint,endVal)
            else:
                output.append([startVal,endVal])
        return output
