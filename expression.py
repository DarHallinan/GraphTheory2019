class state:
    label = None
    edge1 = None
    edge2 = None

class nfa:
    intial = None
    accept = None

    def __init__(self, initial, accept):
      self.intial = initial
      self.accept = accept

def compile(pofix):
    nfaStack = []

    for c in pofix:
        # join the initial and accept states together to create a loop for your characters
        if c == '*':
            nfa = nfaStack.pop()
            initial = state()
            accept = state()

            initial.edge1 = nfa.intial
            initial.edge2 = accept
            nfa.accept.edge1 = nfa.intial
            nfa.accept.edge2 = accept
            nfaStack.append(nfa(initial, accept))

        # merge the two automata by linking 1's accept to 2's initial states
        elif c == '.': 
            nfa2 = nfaStack.pop()
            nfa1 = nfaStack.pop()
            nfa1.accept.edge1 = nfa2.intial
            nfaStack.append(nfa1.intial, nfa2.accept)
        
        # create new initial and accept states and use them to link nfa1 and nfa2
        elif c == '|':
            nfa2 = nfaStack.pop()
            nfa1 = nfaStack.pop()
            initial = state()
            accept = state()

            initial.edge1 = nfa1.intial
            initial.edge2 = nfa2.intial
            # both old accept states now point to our new accept state
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept
            nfaStack.append(nfa(initial, accept))
        
        # creates new states and edges
        # labels each edge with what the current non-special character is
        else:
            accept = state()
            initial = state()
            initial.label = c
            initial.edge1 = accept
            # create instance of class nfa()
            nfaStack.append(nfa(initial, accept))
    
    # should only ever have one nfa in the stack
    return nfaStack.pop()

print(compile("ab.cd.|"))