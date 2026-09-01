class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''

            s = aab
            a | a | b
            a | ab -> pallindore 
            aa | b
            indx
            for i in range(len(s)):
                every possible c split - i.e. substring 
        '''

        res = []
        n = len(s)
        def isPallindrome(str_):
            l, r = 0, len(str_)-1

            while l < r:
                if str_[l] != str_[r]:
                    return False
                l+=1
                r-=1
            return True

        def splitAndCheck(indx, sub_list):
            if indx == n:
                res.append(list(sub_list))
                return

            for i in range(indx, n):
                sub_str = s[indx : i+1]
                if isPallindrome(sub_str):
                    sub_list.append(sub_str)
                    splitAndCheck(i+1, sub_list)
                    sub_list.pop()

                

        splitAndCheck(0, [])

        return res
