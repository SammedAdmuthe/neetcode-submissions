class Solution:
    def isHappy(self, n: int) -> bool:

        def findSumOfSquareOfDigit(num):
            sum_ = 0
            while num!=0:
                sum_ = sum_ + (num % 10)**2
                num//=10
            return sum_


        slow = n
        fast = findSumOfSquareOfDigit(n)


        while fast != 1:
            if slow == fast:
                return False
            slow = findSumOfSquareOfDigit(slow)
            fast = findSumOfSquareOfDigit(findSumOfSquareOfDigit(fast))
        return True