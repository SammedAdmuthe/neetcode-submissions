class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
            len = 3
            A = [1, 2,  3 | 4]
            B = [1 | 4, 4, 5]

            if b_right < a_left:
                move A to left
                move B to right
            if b_left > a_right
                move B to left
                move A to right

            if n is even : 
                (pick a_left + b_left)//2

            1 2 3 4 5 6
            1 2 3
            i = 2
            half - (i + 1) - 1 
        '''
        m, n = len(nums1), len(nums2)

        total = (m+n)
        half = (m+n)//2
        if n < m:
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1)-1
        while (True):
            i = l + (r - l)//2
            j = half - i - 2

            a_left = nums1[i] if i >= 0 else -math.inf
            b_left = nums2[j] if j >= 0 else -math.inf
            a_right = nums1[i+1] if i+1 < len(nums1) else math.inf
            b_right = nums2[j+1] if j+1 < len(nums2) else math.inf          

            if a_left <= b_right and b_left <= a_right:

                if total % 2 == 0:
                    return (max(a_left, b_left) + min(a_right, b_right))/2
                return min (a_right, b_right)

            
            if a_left > b_right:
                r = i - 1
            else:
                l = i + 1

        return -1
