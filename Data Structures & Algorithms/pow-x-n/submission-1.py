class Solution:
    def myPow(self, x: float, n: int) -> float:
        """

            2 Pow 10
            (2 * 2, pow 5)
            (4 * 4, pow 2)
            (16 *16, pow 1)

            2 pow 2

            1 * 2 pow 1
            

        
        """
        if x == 0:
            return 0
        def calcPower(n):

            if n == 0:
                return 1

            res = calcPower(n//2)
            res = res * res
            return res * x if n % 2 else res
        
        res = calcPower(abs(n))

        return res if n>=0 else 1/res