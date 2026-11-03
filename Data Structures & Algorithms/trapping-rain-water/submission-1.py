class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        '''

                0 2 0 3 -> 2
                maxRight maxLeft

               res = curr -  min (maxRight, maxLeft)

        '''
        water = 0
        maxLeft, maxRight = 0, 0
        while l < r:
            
            if height[l] < height[r]:
                maxLeft = max(maxLeft, height[l])
                water += maxLeft - height[l]
                l+=1
            else:
                maxRight = max(maxRight, height[r])
                water += maxRight - height[r]
                r-=1

        return water