class Solution:

    def encode(self, strs: List[str]) -> str:
        """
            ["abc", "def"]
        """
        res = []

        for i in range(len(strs)):
            res.append(str(len(strs[i])))
            res.append("#")
            res.append(strs[i])

        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # 4#Hellow
        while i < len(s):
            j = i
            while s[j] !='#':
                j+=1
            
            
            len_ = int(s[i:j])
            j+=1
            ch_ = s[j:j+len_]
            res.append(ch_)
            i = j + len_
        return res

