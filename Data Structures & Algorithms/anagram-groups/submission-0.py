class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            1010000..1..00 : [act, cat]
            char[26]: Strings[]

        '''
        def encode(str_):
            c = [0] * 26

            for ch in str_:
                c[ord(ch) - ord('a')]+=1
            return "".join([ chr(count) for count in c])

        anagram_group = defaultdict(list)
        for str_ in strs:

            key = encode(str_)
            anagram_group[key].append(str_)
        
        
        return list(anagram_group.values())
