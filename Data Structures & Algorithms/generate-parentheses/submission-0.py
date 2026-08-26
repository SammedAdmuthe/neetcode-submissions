class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        res = []

        def explore(count_open, count_close, constructed):

            if count_open < count_close or count_open> n or count_close > n:
                return

            if count_open == n and count_close == n:
                print(constructed)
                res.append("".join(constructed))
                return

            

            constructed.append('(')
            explore(count_open+1, count_close, constructed)
            constructed.pop()
            constructed.append(')')
            explore(count_open, count_close+1, constructed)
            constructed.pop()


        explore(0, 0, [])
        return res