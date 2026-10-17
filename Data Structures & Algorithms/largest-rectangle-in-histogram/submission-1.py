class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        monotnic increasing stack
        indx, count
        (1, 2),(2, 4)
        1*. 6
        '''

        stack = []
        res = 0

        for i in range(len(heights)):
            count = 1

            while stack and stack[-1][0]>=heights[i]:
                l, b = stack.pop()
                count+=b
                res = max(res, l * (count - 1))
            stack.append((heights[i], count))

        
        width = 0
        while stack:
            h, count = stack.pop()
            width += count
            res = max(res, h * width)
        return res