####################################

Third Year Graph Theory Project 2019

####################################

This is a simple program that generates a non-deterministic finite automaton(NFA) from a regular expression. It then uses that NFA to query the regular expression against text to check if there's a match.

To do this, you must first be able to take in a regular expression. These are usually written in infix notation, how a person would read it but to make it quicker/easier for the computer to read the expression I converted it into postfix notation using the 'Shunting Yard Algorithm'. This involves moving operators onto a stack and printed in the expression according to their precedence.

my shunt() function passes on the expression, now written in postfic notation, onto my compiler. The compiler then creates an empty NFA with an arbitrary initial and accept state. Operands are just added in as labels to the imaginary NFA diagram, while the operators take some more work. For this we need an if/elif statement for all of our operators; 

'*': The Kleene Star - This is the symbol that puts the states in a loop as it means one or more.

'|': The or operator - This is the 'or' operator and creates a new accept state and points the two previous accept states to our new one.

'.': The append operator - this simply takes the accept state of our first NFA and links it to the initial state of the second NFA, concatenating the two.

The compiler then adds all of this into one NFA in the stack and pops it off to the match() function.

Using all this logic, the computer builds an NFA that can now be used to compare the postfix expression against any string of text.

My helper() function follows any 'E', or empty sets and returns the NFA states. This function isn't totally necessary but it does make the final function much tidier and easier to understand.

Finally we have the match() function, this puts everything together. It reads in the regular expression, sends it off to the shunting function and passes the following postfix expression to the compiler. It cycles through every state in the NFA and compares it against every character in the comparative string. Because of this, it only returns a simple true or false; either it matches or it doesn't.

#######################################

Unfortunately, the project altogether didn't work. I feel like the logic is sound and I have tried a lot of different things to fix it but all of my returns come back as false. Despite the negative result, I found this project very interesting to code as there was a lot of planning required for it. It was a nice change of pace from other projects where you just dive in head first and start coding as this forced me to do research online before writing any code. This is also the first Python project we've been given as part of the course and I was excited to get a chance to learn it properly.

#######################################

References:

http://www.oxfordmathcenter.com/drupal7/node/628
https://inventwithpython.com/blog/2012/07/09/16-common-python-runtime-errors-beginners-find/
