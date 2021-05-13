# WRITE YOUR NAME and YOUR COLLABORATORS HERE
#Name: Hongqi Guo
#student ID:011552159
#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the HELPER FUNCTIONS to push and pop values on the opstack 
# Remember that there is a Postscript operator called "pop" so we choose 
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    if (len(opstack) == 0):
        print("Error")
    else:
        return opstack.pop(-1)

    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)


#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to 
# define name, and to lookup a name
def dictPop():
    if (len(dictstack) == 0):
        print("Error")
    else:
        return dictstack.pop(-1)

    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)
    #dictPush pushes the dictionary ‘d’ to the dictstack. 
    #Note that, your interpreter will call dictPush only when Postscript 
    #“begin” operator is called. “begin” should pop the empty dictionary from 
    #the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    dictstack.append({name: value})
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and 
    #call the “define” function.

def lookup(name):

    names = '/' + name
    for item in dictstack:
        if names in item:
            string = item[names]
    return string
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.


#--------------------------- 10% -------------------------------------
# Arithmetic, comparison, and boolean operators: add, sub, mul, eq, lt, gt, and, or, not 
# Make sure to check the operand stack has the correct number of parameters 
# and types of the parameters are correct.
def add():
    x = opPop()
    y = opPop()
    opPush(x+y)
def sub():
    x = opPop()
    y = opPop()
    opPush(y-x)

def mul():
    x = opPop()
    y = opPop()
    opPush(x*y)

def eq():
    x = opPop()
    y = opPop()
    if x == y:
        opPush(True)
    else:
        opPush(False)

def lt():
    x = opPop()
    y = opPop()
    if y < x:
        opPush(True)
    else:
        opPush(False)


def gt():
    x = opPop()
    y = opPop()
    if y > x:
        opPush(True)
    else:
        opPush(False)

def psAnd():
    x = opPop()
    y = opPop()
    if y == True:
        opPush(x)
    else:
        opPush(y)    

def psOr():
    x = opPop()
    y = opPop()
    if y == True:
        opPush(y)
    else:
        opPush(x)

def psNot():
    x = opPop()
    if x == True:
        opPush(False)
    else:
        opPush(True)

#--------------------------- 25% -------------------------------------
# Array operators: define the string operators length, get, getinterval, put, putinterval
def length():
    if len(opstack) == 0:
        print("Error")
    else:
        string = opPop()
        opPush(len(string))

def get():
    if len(opstack) == 0:
        print("Error")
    else:
        index = opPop()
        string = opPop()
        opPush((string[index]))

def getinterval():
    if len(opstack) == 0:
        print("Error")
    else:
        index1 = opPop()
        index2 = opPop()
        string = opPop()
        opPush(string[index2:index1+index2])

def put():
    if len(opstack) == 0:
        print("Error")
    else:
        index1 = opPop()
        index2 = opPop()
        string = opPop()
        string.pop(index2)
        string.insert(index2,index1)




def putinterval():
    if len(opstack) == 0:
        print("Error")
    else:
        index1 = opPop()
        index2 = opPop()
        string = opPop()
        del string[index2:len(index1)+index2]
        string[index2:index2] = index1


#--------------------------- 15% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, mark, cleartomark, counttotmark
def dup():
    if (len(opstack) == 0):
        print("Error")
    else:
        string = opPop()
        opPush(string)
        opPush(string)


def copy():
    index = opPop()
    newstr = []
    i = i1 = i2 = 0
    for i in range(index):
        string = opPop()
        newstr.append(string)
        i += 1    
    for i1 in range(index):
        opPush(newstr[i - 1])
        i -= 1  
        i1 += 1
    for i2 in range(index):
        opPush(newstr[i - 1])
        i -= 1
        i2+= 1

def count():
    x = 0
    for i in opstack:
        x += 1
        i = i
    return x

def pop():
    opPop()

def clear():
    opstack.clear()

def exch():
    x = opPop()
    y = opPop()
    opPush(x)
    opPush(y)

def mark():
    opPush('-mark-')

def cleartomark():
    for i in list(reversed(opstack)):
        if i == '-mark-':
            return opPop()
        else:
            opPop()

def counttomark():
    x = '-mark-'
    y = list(reversed(opstack))
    return opPush(y.index(x))

def stack():
    for i in opstack:
        print(i)

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    x = opPop()
    for i in range(x):
        opPush(dict())
        i = i

def begin():
   x = opPop()
   dictstack.append(x)

def end():
    dictPop()

def psDef():
    if len(opstack) == 0:
        print("Error")        
    else:
        value = opPop()
        key = opPop()
        define(key, value)




#############
def div():
    x = opPop()
    y = opPop()
    if x  is int:
        if y is int:
            opPush(x/y)
        else:
            print('Error,first argument is not int or flort')
    else:
        print('Error,second argument is not int or flort')

