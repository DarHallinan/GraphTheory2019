# Darren Hallinan - G00342845
# Graph Theory Project 2019

def shuntingYard(input):
    infix = ''
    # the user's input will be treated as an infix expression
    input = infix

    operators = {'*': 30, '.': 20, '|': 10}

    postfix, stack = ' ', ' '

    for c in infix:
        # open brackets are pushed straight to stack
        if c == '(': 
            stack += c
        # discard closing bracket, print inside brackets
        elif c == ')':
            while stack[-1] != '(':
                postfix += stack[-1]
                stack = stack[:-1]
            stack = stack[:-1]
        # operators get pushed to stack
        elif c in operators:
            # pushes operator with higher precedence on the stack
            while stack and operators.get(c, 0) <= operators.get(stack[-1], 0):
                postfix += stack[-1]
                stack = stack[:-1]
            stack += c
        else:
            postfix += c
    
    # copied from above to run if stack is not empty
    while stack:
        postfix += stack[-1]
        stack = stack[:-1]
    
    return postfix

print(shuntingYard("(a.b)|(c*.d)"))