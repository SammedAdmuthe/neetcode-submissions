class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        '''

            [(10, 0), (8, 2)]
            [3, 1, 2, 1, 0, 0]

            10 8 5 11
        '''

        stack=[]
        res = [0] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                indx = stack.pop()
                res[indx] += 1
            if stack:
                res[stack[-1]] += 1
            stack.append(i)

        return res
