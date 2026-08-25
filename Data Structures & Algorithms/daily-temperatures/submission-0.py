class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i, temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:

                popped_temp, popped_indx = stack.pop()

                res[popped_indx] = i - popped_indx

            stack.append((temp, i))

        return res