# WRITE YOUR NAME and YOUR COLLABORATORS HERE
#011552159
# Hongqi Guo
# ------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  # assuming top of the stack is the end of the list


# Now define the HELPER FUNCTIONS to push and pop values on the opstack
# Remember that there is a Postscript operator called "pop" so we choose
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    if (len(opstack) == 0):
        print("Error: opstack is empty")
    else:
        return opstack.pop()

    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.


def opPush(value):
    opstack.append(value)


# -------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  # assuming top of the stack is the end of the list


# now define functions to push and pop dictionaries on the dictstack, to
# define name, and to lookup a name
def dictPop():
    if (len(dictstack) == 0):
        print("Error: dictstack is empty")
    else:
        return dictstack.pop(-1)

    # dictPop pops the top dictionary from the dictionary stack.


def dictPush(d):
    dictstack.append(d)
    # dictPush pushes the dictionary ‘d’ to the dictstack.
    # Note that, your interpreter will call dictPush only when Postscript
    # “begin” operator is called. “begin” should pop the empty dictionary from
    # the opstack and push it onto the dictstack by calling dictPush.


def define(key, value):
    if (len(dictstack) == 0):
        d = {key: value}
        dictPush((0,d))
    else:
        (index, d) = dictPop()  # grab topmost dict in dictstacks
        d[key] = value  # add or overwrite current key name with new value
        dictPush((index, d))
    # add name:value pair to the top dictionary in the dictionary stack.
    # Keep the '/' in the name constant.
    # Your psDef function should pop the name and value from operand stack and
    # call the “define” function.

def lookup(name, scope):
    queryName = '/' + name
    # for item in reversed(dictstack):
    #     if queryName in item:
    #         return item[queryName]

    if scope == "static":
        index = staticLink(queryName)
        if index == None:
            print("Error: NAME " + queryName + " is undefined in dictstack")
            return None
        else:
            (link, d) = dictstack[index]
            return d[queryName]
    else:
        for (l, d) in reversed(dictstack):
            if queryName in d:
                return d[queryName]

    print("Error: NAME " + name + " is undefined in dictstack")
    return None
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.


# --------------------------- 10% -------------------------------------
# Arithmetic, comparison, and boolean operators: add, sub, mul, eq, lt, gt, and, or, not
# Make sure to check the operand stack has the correct number of parameters
# and types of the parameters are correct.
def add():
    if len(opstack) >= 2:
        op2 = opstack[-1]
        op1 = opstack[-2]
        if isinstance(op2, int) and isinstance(op1, int):
            op2 = opPop()
            op1 = opPop()
            opPush(op1 + op2)
        else:
            print("Error: add - one of the operands is not a numerical value")
    else:
        print("Error: add expects 2 operands")


def sub():
    if len(opstack) >= 2:
        var1 = opstack[-1]
        var2 = opstack[-2]
        if isinstance(var1, int) and isinstance(var2, int):
            var1 = opPop()
            var2 = opPop()
            opPush(var2 - var1)
        else:
            print("Error: sub - one of the operands is not a numerical value")
    else:
        print("Error: sub expects 2 operands")


def mul():
    if len(opstack) >= 2:
        var1 = opstack[-1]
        var2 = opstack[-2]
        if isinstance(var1, int) and isinstance(var2, int):
            var1 = opPop()
            var2 = opPop()
            opPush(var2 * var1)
        else:
            print("Error: mul - one of the operands is not a numerical value")
    else:
        print("Error: mul expects 2 operands")


def eq():
    if len(opstack) >= 2:
        var1 = opstack[-1]
        var2 = opstack[-2]
        if type(var1) == type(var2):
            var1 = opPop()
            var2 = opPop()
            opPush(var1 == var2)
        else:
            print("Error: eq - two operandss are incompatable types")
    else:
        print("Error: eq expects 2 operands")


def lt():
    if len(opstack) >= 2:
        var1 = opstack[-1]
        var2 = opstack[-2]
        if type(var1) == type(var2):
            var1 = opPop()
            var2 = opPop()
            opPush(var1 > var2)
        else:
            print("Error: lt - two operandss are incompatable types")
    else:
        print("Error: lt expects 2 operands")


def gt():
    if len(opstack) >= 2:
        var1 = opstack[-1]
        var2 = opstack[-2]
        if type(var1) == type(var2):
            var1 = opPop()
            var2 = opPop()
            opPush(var1 < var2)
        else:
            print("Error: gt - two operandss are incompatable types")
    else:
        print("Error: gt expects 2 operands")


def psAnd():
    if len(opstack) >= 2:
        var1 = opstack[-1]
        var2 = opstack[-2]
        if isinstance(var1, bool) and isinstance(var2, bool):
            var1 = opPop()
            var2 = opPop()
            opPush(var1 and var2)
        else:
            print("Error: and - one of the operands is not a boolean value")
    else:
        print("Error: and expects 2 operands")


def psOr():
    if len(opstack) >= 2:
        var1 = opstack[-1]
        var2 = opstack[-2]
        if isinstance(var1, bool) and isinstance(var2, bool):
            var1 = opPop()
            var2 = opPop()
            opPush(var1 or var2)
        else:
            print("Error: or - one of the operands is not a boolean value")
    else:
        print("Error: or expects 2 operands")


def psNot():
    if len(opstack) >= 1:
        var1 = opstack[-1]
        if isinstance(var1, bool):
            var1 = opPop()
            opPush(not var1)
        else:
            print("Error: not - operand is not a boolean value")
    else:
        print("Error: not expects 1 operand")


# --------------------------- 25% -------------------------------------
# Array operators: define the string operators length, get, getinterval, put, putinterval
def length():
    if len(opstack) >= 1:
        var1 = opstack[-1]
        if isinstance(var1, list):
            opPush(len(opPop()))
        else:
            print("Error: length - operand is not an array")
    else:
        print("Error: length expects 1 operand")


def get():
    if len(opstack) >= 2:
        var1 = opstack[-1]
        var2 = opstack[-2]
        if isinstance(var1, int) and isinstance(var2, list):
            var1 = opPop()
            var2 = opPop()
            opPush(var2[var1])
        else:
            print("Error: get - incompatable types")
    else:
        print("Error: get expects 2 operands")


def getinterval():
    if len(opstack) >= 3:
        index1 = opPop()
        index2 = opPop()
        var3 = opPop()
        if isinstance(index1, int) and isinstance(index2, int) and isinstance(var3, list):
            opPush(var3[index2:index1 + index2])
        else:
            print("Error: getinterval - incompatable types")
    else:
        print("Error: getinterval expects 3 operands")


def put():
    if len(opstack) >= 3:
        index1 = opPop()
        index2 = opPop()
        var3 = opPop()
        if isinstance(index1, int) and isinstance(index2, int) and isinstance(var3, list):
            var3.pop(index2)
            var3.insert(index2, index1)
        else:
            print("Error: put - incompatable types")
    else:
        print("Error: put expects 3 operands")



def putinterval():
    if len(opstack) >= 3:
        list1 = opPop()
        index2 = opPop()
        list2 = opPop()
        if isinstance(list1, list) and isinstance(index2, int) and isinstance(list2, list):
            del list2[index2:len(list1) + index2]
            list2[index2:index2] = list1
        else:
            print("Error: putinterval - incompatable types")
    else:
        print("Error: putinterval expects 3 operands")



# --------------------------- 15% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, mark, cleartomark, counttotmark
def dup():
    if len(opstack) >= 1:
        var1 = opstack[-1]
        opPush(var1)
    else:
        print("Error: dup expects 1 operand")


def copy():
    if len(opstack) >= 2:
        n = opPop()
        if isinstance(n, int):
            temp = []
            for i in range(n):
                temp.append(opstack[-i])
            for i in range(n):
                opPush(temp.pop())
        else:
            print("Error: copy - incompatable operands")
    else:
        print("Error: copy expects 1 operand")


def count():
    opPush(len(opstack))


def pop():
    opPop()


def clear():
    opstack.clear()


def exch():
    if len(opstack) >= 2:
        var1 = opPop()
        var2 = opPop()
        opPush(var1)
        opPush(var2)
    else:
        print("Error: exch expects 2 operands")


def mark():
    opPush('-mark-')


def cleartomark():
    return_list =[]
    for i in reversed(opstack):
        if i == '-mark-':
            opPop()
            return return_list[::-1]
        else:
            return_list.append(opPop())


def counttomark():
    x = '-mark-'
    y = list(reversed(opstack))
    opPush(y.index(x))


def stack():
    print("==============")
    for item in opstack[::-1]:
        print(item)

    dictstack_length = len(dictstack) - 1

    print("==============")
    for (index, item) in reversed(list(enumerate(dictstack))):
        cur_top_stack, d = item
        print("----" + str(index) + "----" + str(cur_top_stack) + "----")
        if d != {}:
            for k in d:
                print(k, d[k])
    print("==============")


# --------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    if len(opstack) >= 1:
        opPop()
        opstack.append({})
    else:
        print("Error: dict expects 1 operand")


def begin():
    if len(opstack) >= 1:
        var1 = opstack[-1]
        if isinstance(var1, dict):
            dictPush(opPop())
    else:
        print("Error: begin expects 1 operand")


def end():
    if len(dictstack) >= 1:
        dictPop()
    else:
        print("Error: end expects 1 operand")


def psDef():
    if len(opstack) >= 2:
        value = opPop()
        key = opPop()
        define(key, value)
    else:
        print("Error: def expects 2 operands")


def psForAll(scope):
    if len(opstack) >= 2:
        code = opPop()
        inputArray = opPop()

        for item in inputArray:
            opPush(item)
            interpretSPS(code, scope)
    else:
        print("Error: forAll expects 2 operands")

def psRepeat(scope):
    if len(opstack) >= 2:
        codeArray = opPop()
        repeatTimes = opPop()

        for _ in range(repeatTimes):
            interpretSPS(codeArray, scope)
    else:
        print("Error: repeat expects 2 operands")


def psIf(scope):
    if len(opstack) >= 2:
        op2 = opPop()
        op1 = opPop()
        if isinstance(op2, dict):
            if op1:
                interpretSPS(op2, scope)
        else:
            opPush(op1)
            opPush(op2)
            print("Error: if - incompatable operands")
    else:
        print("Error: if expects 2 operands")


def psIfelse(scope):
    if len(opstack) >= 3:
        op3 = opPop()
        op2 = opPop()
        op1 = opPop()
        if isinstance(op3, dict) and isinstance(op2, dict):
            if op1:
                interpretSPS(op2, scope)
            else:
                interpretSPS(op3, scope)
        else:
            opPush(op1)
            opPush(op2)
            opPush(op3)
            print("Error: ifelse - incompatable operands")
    else:
        print("Error: ifelse expects 3 operands")

##########################
##PART 2 ##

import re


def tokenize(s):
    return re.findall(
        "/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

def str2int(s):
    try:
        i = int(s)
        return i
    except:
        return s

def process_item(c):
    if len(c) >= 2 and c[0] == '[' and c[-1] == ']':
        array_str = c[1:-1]
        array_str_aplit = array_str.split(" ")
        l = []
        for item in array_str_aplit:
            l.append(str2int(item))
        return l
    elif c.lower() == "true":
        return True
    elif c.lower() == "false":
        return False
    else:
        return str2int(c)

# COMPLETE THIS FUNCTION
# The it argument is an iterator.
# The tokens between '{' and '}' is included as a sub code-array (dictionary). If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return {'codearray': res}
        elif c == '{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner
            # parenthesis, it will be appended to the list we are constructing
            # as a whole.
            res.append(groupMatch(it))
        else:
            res.append(process_item(c))
    return False


# COMPLETE THIS FUNCTION
# Function to parse a list of tokens and arrange the tokens between { and } braces
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested dictionaries.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c == '}':  # non matching closing parenthesis; return false since there is
            # a syntax error in the Postscript code.
            return False
        elif c == '{':
            res.append(groupMatch(it))
        else:
            res.append(process_item(c))
    return {'codearray': res}


# all functions
functions = {'add':add,'sub':sub,'mul':mul,'eq':eq,'lt':lt,'gt':gt,
             'and':psAnd, 'or':psOr, 'not':psNot,
             'length':length, 'get':get, 'getinterval':getinterval, 'put':put,'putinterval':putinterval,
             "begin": begin, "end": end,
             'dup':dup, 'copy':copy, 'count':count, 'pop':pop, 'clear':clear, 'exch':exch, 'mark':mark, 'cleartomark':cleartomark,'counttomark':counttomark,
             'dict':psDict,'def':psDef,'stack':stack}
scope_functions = {'forall':psForAll, 'repeat':psRepeat, 'if':psIf, 'ifelse':psIfelse, }
types = [int, bool]

# COMPLETE THIS FUNCTION
# This will probably be the largest function of the whole project,
# but it will have a very regular and obvious structure if you've followed the plan of the assignment.
# Write additional auxiliary functions if you need them.
def interpretSPS(code, scope):  # code is a code array
    if type(code) == dict:
        code_new = code.get("codearray")
    else:
        code_new = code

    link = 0
    for c in code_new:
        if isinstance(c, list):
            mark()
            interpretSPS(c, scope)
            c_parse = cleartomark()
            opPush(c_parse)

        # code_array map
        elif isinstance(c, dict):
            opPush(c)
        elif (type(c) in types):
            opPush(c)
        elif ((type(c) is str)):
            if (c.startswith("/")):
                opPush(c)
            elif c.lower() == "true":
                opPush(True)
            elif c.lower() == "false":
                opPush(False)
            elif c in functions:
                func = functions[c]
                func()
            elif c in scope_functions:
                scope_func = scope_functions[c]
                scope_func(scope)
            else:
                lookup_result = lookup(c, scope)
                if lookup_result is None:
                    print("lookup error")
                elif isinstance(lookup_result, list):
                    opPush(lookup_result)
                elif isinstance(lookup_result, dict):
                    if scope == "static":
                        link = staticLink(str(c))
                        if link != None:
                            dictPush((link, {}))
                            interpretSPS(lookup_result, scope)
                            dictPop()
                    elif scope == "dynamic":
                        dictPush((link, {}))
                        interpretSPS(lookup_result, scope)
                        dictPop()
                    # interpretSPS(lookup_result, scope)
                else:
                    opPush(lookup_result)


def interpreter(s, scope):
    code_map = parse(tokenize(s))
    if "codearray" not in code_map:
        return None
    interpretSPS(code_map.get("codearray"), scope)

def staticLink(name):
    dictstack_length = len(dictstack)
    if name[0] != '/':
        name = "/" + name
    if dictstack_length == 0:
        return None

    current_index = dictstack_length - 1
    while True:
        for item in dictstack[current_index][1]:
            if name in item:
                return current_index

        if current_index == 0:
            return None
        else:
            current_index = dictstack[current_index][0]


# clear opstack and dictstack
def clearStacks():
    opstack[:] = []
    dictstack[:] = []

def clearBoth():
    opstack[:] = []
    dictstack[:] = []

def sspsTests():
    testinput1 = """
    /x 4 def
    /g { x stack } def
    /f { /x 7 def g } def
    f
    """
    testinput2 = """
    /x 4 def
    [1 1 1] dup 1 [2 3] putinterval /arr exch def
    /g { x stack } def
    /f { 0 arr {7 mul add} forall /x exch def g } def
    f
    """
    testinput3 = """
    /m 50 def
    /n 100 def
    /egg1 {/m 25 def n} def
    /chic
    	{ /n 1 def
	      /egg2 { n stack} def
	      m  n
	      egg1
	      egg2
	    } def
    n
    chic
        """
    testinput4 = """
    /x 10 def
    /A { x } def
    /C { /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """
    testinput5 = """
    /x 10 def
    /n 5  def
    /A { 0  n {x add} repeat} def
    /C { /n 3 def /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """
    testinput6 = """
    /out true def 
    /xand { true eq {pop false} {true eq { false } { true } ifelse} ifelse dup /x exch def stack} def 
    /myput { out dup /x exch def xand } def 
    /f { /out false def myput } def 
    false f
    """
    testinput7 = """
    /x [1 2 3 4] def
    /A { x length } def
    /C { /x [10 20 30 40 50 60] def A stack } def
    /B { /x [6 7 8 9] def /A { x 0 get} def C } def
    B
    """
    testinput8 = """
    [0 1 2 3 4 5 6 7 8 9 10] 3 4 getinterval /x exch def
    /a 10 def  
    /A { x length } def
    /C { /x [a 2 mul a 3 mul dup a 4 mul] def A  a x stack } def
    /B { /x [6 7 8 9] def /A { x 0 get} def /a 5 def C } def
    B
    """

    mytestinput1 = """
    /a 4 def
    /tri { a a a mul mul } def
    /h { /a 5 def tri /q { a } def /n { a } def stack q n } def
    h
    """
        # output = """
        # Static
        # ==============
        # 64
        # ==============
        # ----1----0----
        # /a 5
        # /q {'codearray': ['a']}
        # /n {'codearray': ['a']}
        # ----0----0----
        # /a 4
        # /tri {'codearray': ['a', 'a', 'a', 'mul', 'mul']}
        # /h {'codearray': ['/a', 5, 'def', 'tri', '/q', {'codearray': ['a']}, 'def', '/n', {'codearray': ['a']}, 'def', 'stack', 'q', 'n']}
        # ==============
        # Dynamic
        # ==============
        # 125
        # ==============
        # ----1----0----
        # /a 5
        # /q {'codearray': ['a']}
        # /n {'codearray': ['a']}
        # ----0----0----
        # /a 4
        # /tri {'codearray': ['a', 'a', 'a', 'mul', 'mul']}
        # /h {'codearray': ['/a', 5, 'def', 'tri', '/q', {'codearray': ['a']}, 'def', '/n', {'codearray': ['a']}, 'def', 'stack', 'q', 'n']}
        # ==============
        # """
    mytestinput2 = """
    /addnew { 4 num add } def
    /x 2 def
    /num x def
    /mulnew { /x 5 def num addnew mul stack } def
    /comp {
            /num x def 
            /add { 2 num add } def 
             mulnew
        } def
        comp
    """
        # output = """
        # Static
        # ==============
        # 12
        # ==============
        # ----2----0----
        # /x 5
        # ----1----0----
        # /num 2
        # /add {'codearray': [2, 'num', 'add']}
        # ----0----0----
        # /addnew {'codearray': [4, 'num', 'add']}
        # /x 2
        # /num 2
        # /mulnew {'codearray': ['/x', 5, 'def', 'num', 'addnew', 'mul', 'stack']}
        # /comp {'codearray': ['/num', 'x', 'def', '/add', {'codearray': [2, 'num', 'add']}, 'def', 'mulnew']}
        # ==============
        # Dynamic
        # ==============
        # 12
        # ==============
        # ----2----0----
        # /x 5
        # ----1----0----
        # /num 2
        # /add {'codearray': [2, 'num', 'add']}
        # ----0----0----
        # /addnew {'codearray': [4, 'num', 'add']}
        # /x 2
        # /num 2
        # /mulnew {'codearray': ['/x', 5, 'def', 'num', 'addnew', 'mul', 'stack']}
        # /comp {'codearray': ['/num', 'x', 'def', '/add', {'codearray': [2, 'num', 'add']}, 'def', 'mulnew']}
        # ==============
        # """
    mytestinput3 = """
    /x 1 def
    /fun {
        /x x 2 add def
    } def
    /A { x fun mul } def
    /B { /x 3 def /A { x stack } def /C { /x 8 def A } def C } def
    B
    """
        # output = """
        # Static
        # ==============
        # 3
        # ==============
        # ----3----1----
        # ----2----1----
        # /x 8
        # ----1----0----
        # /x 3
        # /A {'codearray': ['x', 'stack']}
        # /C {'codearray': ['/x', 8, 'def', 'A']}
        # ----0----0----
        # /x 1
        # /fun {'codearray': ['/x', 'x', 2, 'add', 'def']}
        # /A {'codearray': ['x', 'fun', 'mul']}
        # /B {'codearray': ['/x', 3, 'def', '/A', {'codearray': ['x', 'stack']}, 'def', '/C', {'codearray': ['/x', 8, 'def', 'A']}, 'def', 'C']}
        # ==============
        # Dynamic
        # ==============
        # 8
        # ==============
        # ----3----0----
        # ----2----0----
        # /x 8
        # ----1----0----
        # /x 3
        # /A {'codearray': ['x', 'stack']}
        # /C {'codearray': ['/x', 8, 'def', 'A']}
        # ----0----0----
        # /x 1
        # /fun {'codearray': ['/x', 'x', 2, 'add', 'def']}
        # /A {'codearray': ['x', 'fun', 'mul']}
        # /B {'codearray': ['/x', 3, 'def', '/A', {'codearray': ['x', 'stack']}, 'def', '/C', {'codearray': ['/x', 8, 'def', 'A']}, 'def', 'C']}
        # ==============
        # """
    ssps_testinputs = [testinput1, testinput2, testinput3, testinput4, testinput5, testinput6, testinput7, testinput8,mytestinput1,mytestinput2,mytestinput3]
    i = 1
    for input in ssps_testinputs:
        print('TEST CASE -',i)
        i += 1
        print("Static")
        interpreter(input, "static")
        clearBoth()
        print("Dynamic")
        interpreter(input, "dynamic")
        clearBoth()
        print('\n-----------------------------')

if __name__ == "__main__":
    sspsTests()
