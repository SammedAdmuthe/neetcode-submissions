class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        '''
            i, j

            if i == j:
                return i+1 , j+1
            
            delete -> i+1, j
            replace -> i+1, j+1
            insert -> i, j+1


                add              replace                     delete
        add replace delete.   add.  replace delete.     add. replace delete. 

        '''
        
        dp = {}
        def editDistance(i, j):


            if i == len(word1) and j == len(word2):
                return 0
            delete, insert, replace = math.inf, math.inf, math.inf
            

            if (i, j) in dp:
                return dp[(i, j)]


            if i < len(word1) and j < len(word2) and word1[i] == word2[j]:   
                return editDistance(i+1, j+1)

            if i < len(word1):
                delete = 1 + editDistance(i+1, j)

            if i < len(word1) and j < len(word2):
                replace = 1 + editDistance(i+1, j+1)
            
            if j < len(word2):
                insert = 1 + editDistance(i, j+1)

            dp[(i, j)] = min (delete, replace, insert) 
            return  min (delete, replace, insert)

        return editDistance(0, 0)
