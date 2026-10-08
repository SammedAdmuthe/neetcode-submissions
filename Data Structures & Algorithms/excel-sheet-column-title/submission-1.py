class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        '''

            32 %26 = 6
            32//26 = 1

            100 % 26 = 4 and 

            ord(c) - ord('A') + 1 = digit
        '''


        res = []
        while columnNumber > 0:
            c = ((columnNumber - 1) % 26) + ord('A')
            res.append(chr(c))
            (columnNumber) = (columnNumber - 1) // 26

        res.reverse()

        return "".join(res)