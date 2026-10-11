class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)

        if num1 == '0' or num2 == "0":
            return '0'

        res = [0] * (m + n)
        for j in range(n-1, -1, -1):
            n2 = int(num2[j])
            indx = m + n - 1 - (n - j - 1)
            for i in range(m-1, -1, -1):
                n1 = int(num1[i])

                product = n1 * n2
                sum_ = product % 10
                res[indx] += sum_
                res[indx-1] += product // 10 + res[indx]  // 10
                res[indx] %= 10
                indx-=1
        
        i = 0
        while res[i]==0:
            i+=1
        return "".join(map(str, res[i:]))
                