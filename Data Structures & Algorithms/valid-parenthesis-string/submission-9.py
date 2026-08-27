class Solution:
    def checkValidString(self, s: str) -> bool:
        '''

            open == close


            if * is (

            if * is )
            else

        '''
        dp = {}
        def checkIfValid(indx, open_):
            if indx == len(s):
                return open_ == 0

            if open_ < 0:
                return False
            
            if (indx, open_) in dp:
                return dp[(indx, open_)]

            if s[indx] == '*':
                dp[(indx, open_)] = (
                    checkIfValid(indx + 1, open_+1)
                    or checkIfValid(indx + 1, open_-1)
                    or checkIfValid(indx + 1, open_) 
                )
                return dp[(indx, open_)]
            elif s[indx] == '(':
                dp[(indx, open_)] = checkIfValid(indx + 1, open_+1)
                return dp[(indx, open_)]
            else:
                dp[(indx, open_)] = checkIfValid(indx + 1, open_-1)
                return dp[(indx, open_)]
            return False
        
        return checkIfValid(0, 0)
            