class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for s in strs:
            countArr = [0] * 26
            for c in s :
                countArr[ord(c) - ord('a')] += 1
            result[tuple(countArr)].append(s)
       

        return list(result.values())