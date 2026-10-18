class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()

            

        l = 0
        res = []
        for r in range(len(nums)):

            while stack and stack[-1] < nums[r]:
                stack.pop()
            
            stack.append(nums[r])
            if r - l + 1 == k:
                res.append(stack[0])
                if nums[l] == stack[0]:
                    stack.popleft()
                l+=1

        return res