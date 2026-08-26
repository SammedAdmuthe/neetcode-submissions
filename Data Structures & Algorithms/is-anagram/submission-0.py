class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def encode(str_):
            count = [0] * 26
            for c in str_:
                count[ord(c) - ord('a')]+=1

            return "".join(str(c) for c in count)
        
        return encode(s) == encode(t)