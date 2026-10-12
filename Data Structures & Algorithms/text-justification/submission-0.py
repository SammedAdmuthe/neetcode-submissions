class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        

        '''
            each line has a limit of 16

            this - 5
            is - 3
            an - 3 -> 16 - 11 -> 5 
            example - 7

        '''
        def justify(word_list, char_count):
            gaps = len(word_list) - 1
            extra_spaces = maxWidth - char_count
            sentence = []
            spaces = []
            if gaps == 0:
                return word_list[0] + " " * extra_spaces
            gaps_with_additional_space = extra_spaces % gaps
            space_each_gap = extra_spaces // gaps
            print(char_count)


            for i, word in enumerate(word_list):
                if i != len(word_list)-1:
                    sentence.append(word)
                    count_space = space_each_gap
                    if gaps_with_additional_space > 0:
                        count_space +=1
                    space = " " * count_space
                    gaps_with_additional_space -=1
                    sentence.append(space)
                else:
                    sentence.append(word)

            return "".join(sentence)
                
        n = len(words)
        count_so_far = 0
        res = []
        consider = []
        word_count = 0
        for i in range(n):
            word = words[i]

            word_len = len(word)
            word_count+=1
            if count_so_far + word_len + word_count - 1 <= maxWidth:
                count_so_far+=word_len
                consider.append(words[i])
            else:
                sentence = justify(consider, count_so_far)
                res.append(sentence)
                count_so_far = word_len                
                consider = [words[i]]
                word_count = 1
        
        final_sentence = []
        count = 0
        for i, word in enumerate(consider):
            final_sentence.append(word)
            count += len(word)
            if i != len(consider) - 1:
                count+=1
                final_sentence.append(" ")
        final_sentence.append(" " * (maxWidth - count) )
        res.append("".join(final_sentence))
        
        return res