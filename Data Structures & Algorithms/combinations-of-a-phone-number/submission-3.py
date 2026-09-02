class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        


        digit_char = {
            '2' :['a', 'b', 'c'],
            '3' :['d', 'e', 'f'],
            '4' :['g', 'h', 'i'],
            '5' :['j', 'k', 'l'],
            '6' :['m', 'n', 'o'],
            '7' :['p', 'q', 'r', 's'],
            '8' :['t', 'u', 'v'],
            '9' :['w', 'x', 'y', 'z'],
        }

        if not len(digits):
            return []


        res = []
        sub_list = []
        def creat_combination(indx):
            if indx == len(digits):
                res.append("".join(sub_list))
                return



            for chars in digit_char[digits[indx]]:
                sub_list.append(chars)
                creat_combination(indx+1)
                sub_list.pop()

        
        creat_combination(0)
        return res
