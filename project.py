# Darren Hallinan - G00342845
# Graph Theory Project 2019

class state:
    label, edge1, edge2 = None, None, None

class NFA:
    initial, accept = None, None

    def __init__(self, initial, accept):
      self.initial, self.accept = initial, accept

# convert infix notation to postfix
def shunt(infix):
    operators = {'*': 30, '+': 30, '?': 30, '.': 20, '|': 10}
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

# regular expression compiler
def compile(postfix):
    nfaStack = []

    for c in postfix:
        # join the initial and accept states together to create a loop for your characters
        if c == '*':
            nfa = nfaStack.pop()
            initial, accept = state(), state()

            initial.edge1, nfa.accept.edge1 = nfa.initial, nfa.initial
            initial.edge2, nfa.accept.edge2 = accept, accept
            nfaStack.append(NFA(initial, accept))
        # merge the two automata by linking 1's accept to 2's initial states
        elif c == '.': 
            nfa2, nfa1 = nfaStack.pop(), nfaStack.pop()
            nfa1.accept.edge1 = nfa2.initial
            nfaStack.append(NFA(nfa1.initial, nfa2.accept))       
        # create new initial and accept states and use them to link nfa1 and nfa2
        elif c == '|':
            nfa2, nfa1 = nfaStack.pop(), nfaStack.pop()
            initial, accept = state(), state()
            initial.edge1, initial.edge2 = nfa1.initial, nfa2.initial
            # both old accept states now point to our new accept state
            nfa1.accept.edge1, nfa2.accept.edge1 = accept, accept
            nfaStack.append(NFA(initial, accept))      
        # creates new states and edges; labels each edge with what the current non-special character is
        else:
            initial, accept = state(), state()
            initial.label = c
            initial.edge1 = accept
            # create instance of class nfa()
            nfaStack.append(NFA(initial, accept))   
    # should only ever have one nfa in the stack
    return nfaStack.pop()

def helper(state):
    states = set()
    states.add(state)
    # if arrow is labelled as 'E', or empty set
    if state.label is None:
        if state.edge1 is not None:
            states |= helper(state.edge1)
        if state.edge2 is not None:
            states |= helper(state.edge2)
    return states

def match(infix, string):
    # shunt and compile the expression to prepare it for matching
    postfix = shunt(infix)
    nfa = compile(postfix)

    currentS, nextS = set(), set()
    # add initial state to the working set
    currentS |= helper(nfa.initial)

    for s in string:
        for c in currentS:
            if c.label == s:
                nextS |= helper(c.edge1)
        currentS = nextS
        nextS = set()

    return(nfa.accept in currentS)

# Test to make sure eveything works together
testInfixes = ["a.b.c", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
testStrings = ["", "abc", "abbc", "abba", "abcc", "abad", "abbbc"]

for i in testInfixes:
    for s in testStrings:
        print(match(i, s), i, s)