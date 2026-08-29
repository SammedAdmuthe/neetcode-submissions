class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        def isOperator(token):
            return token in ["+", "-", "*", "/"]



        def evalute (num1, num2, operator):
            match operator:
                case "+":
                    return num1 + num2
                case "-":
                    return num2 - num1
                case "*":
                    return num1 * num2
                case "/":
                    if num1 == 0:
                        raise Exception("Divide By Zero Error")
                    return int(num2/num1)

        for token in tokens: # [+, 5, +]
            if isOperator(token):
                if stack:
                    num1, num2 = stack.pop(), stack.pop() # 12/ 132
                    res = evalute(num1, num2, token)
                    stack.append(res)
            else:
                stack.append(int(token)) # stack [10, 6, 0, 17]
        print(stack)
        return stack[0]