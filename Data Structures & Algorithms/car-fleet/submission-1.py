class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = defaultdict()
        stack = []

        for i in range (len(position)):
            dic[position[i]] = speed[i]

        dicSorted = sorted(dic.items(), reverse=True)
        


        for p,s in dicSorted:
            stack.append((target-p)/s)
            ##stack.append((target- p)/dicSorted[p])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        