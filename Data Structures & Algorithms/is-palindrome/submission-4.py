class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1
        def isAlphaNumeric(c):
            if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9'):
                return True
            return False


        while left < right:
            while left < right and not isAlphaNumeric(s[left]):
                left+=1

            while left < right and not isAlphaNumeric(s[right]):
                right-=1

            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1

        return True