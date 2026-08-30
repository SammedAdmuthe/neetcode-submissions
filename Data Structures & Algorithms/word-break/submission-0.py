class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        


        word_dict_set = set(wordDict)
        dp = {}

        def check(i):
            
            if i == len(s):
                return True
            if i in dp:
                return dp[i]

            for j in range(i, len(s)):
                if s[i:j+1] in word_dict_set:
                    if check(j+1):
                        return True
            
            dp[i] = False
            return False


        return check(0)