class Solution:
    def decodeString(self, s: str) -> str:
        '''

            2, [ a 3 [ b

            we need to track the number and push the number when we encounter [
            we also need to track string and multiply it with number when we encounter ]


        '''

        stack = []
        digit = 0
        str_= ""
        for c in s:
            print(stack)
            if c == '[':
                # insert digit in stack
                stack.append(digit)
                stack.append('[')
                digit = 0

            elif c >= 'a' and c <= 'z':
                stack.append(c)

            elif c == ']':
                chars = []

                while stack and stack[-1] != '[':
                    chars.append(stack.pop())
                
                stack.pop() # remove [

                multipler = stack.pop()
                new_str = "".join(chars[::-1]) * multipler
                stack.append(new_str)
            else:
                digit*=10
                digit+= int(c)


        return "".join(stack)
