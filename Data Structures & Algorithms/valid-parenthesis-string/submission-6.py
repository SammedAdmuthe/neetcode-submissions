class Solution:
    def checkValidString(self, s: str) -> bool:
        '''

            open == close


            if * is (

            if * is )
            else

        '''
        dp = {}
        def checkIfValid(indx, open_, close_):
            if indx == len(s):
                return open_ == close_

            if open_ < close_:
                return False
            
            if (indx, open_, close_) in dp:
                return dp[(indx, open_, close_)]

            if s[indx] == '*':
                dp[(indx, open_, close_)] = (
                    checkIfValid(indx + 1, open_+1, close_)
                    or checkIfValid(indx + 1, open_, close_+1)
                    or checkIfValid(indx + 1, open_, close_) 
                )
                return dp[(indx, open_, close_)]
            elif s[indx] == '(':
                dp[(indx, open_, close_)] = checkIfValid(indx + 1, open_+1, close_)
                return dp[(indx, open_, close_)]
            else:
                dp[(indx, open_, close_)] = checkIfValid(indx + 1, open_, close_+1)
                return dp[(indx, open_, close_)]
            return False
        
        return checkIfValid(0, 0, 0)
            