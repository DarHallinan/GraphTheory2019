####################################

Third Year Graph Theory Project 2019

####################################

This is a simple program that generates a non-deterministic finite automaton(NFA) from a regular expression. It then uses that NFA to query the regular expression against text to check if there's a match.

To do this, you must first be able to take in a regular expression. These are usually written in infix notation, how a person would read it but to make it quicker/easier for the computer to read the expression I converted it into postfix notation using the 'Shunting Yard Algorithm'. This involves moving operators onto a stack and printed in the expression according to their precedence.

my shunt() function passes on the expression, now written in postfic notation, onto my compiler. The compiler then creates an empty NFA with an arbitrary initial and accept state. Operands are just added in as labels to the imaginary NFA diagram, while the operators take some more work. For this we need an if/elif statement for all of our operators; 

'*': The Kleene Star - This is the symbol that puts the states in a loop as it means one or more

'|': The or operator - This is the 'or' operator and creates a new accept state and points the two previous accept states to our new one

'.': The append operator - this simply takes the accept state of our first NFA and links it to the initial state of the second NFA, concatenating the two.

Using all this logic, the computer builds an NFA that can now be used to compare the postfix expression against any string of text.
