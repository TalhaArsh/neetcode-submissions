class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # stores index of temp

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                noOfDays = i - stack[-1]
                result[stack[-1]] = noOfDays
                stack.pop()
            stack.append(i)

        return result



        