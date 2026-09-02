class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zeros = 0
        pro_except_zero = 1
        n = len(nums)
        for num in nums:
            if num == 0:
                count_zeros +=1
            else:
                pro_except_zero*=num

        if count_zeros > 1:
            return [0]*n
        
        res = []
        for num in nums:
            if num == 0 and count_zeros == 1:
                res.append(pro_except_zero)
            elif count_zeros == 1:
                res.append(0)
            else:
                res.append(pro_except_zero//num)
        return res