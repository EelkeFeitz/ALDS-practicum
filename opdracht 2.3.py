class mystack:

    def __init__(self):
        self.stack = []

    def push(self, a):
        self.stack.append(a)

    def pop(self):
        self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def isEmpty(self):
        return not bool(len(self.stack))


"""""
is_correct_string(s)
    Takes a string and checks if every sort of opening bracket has the corresponding closing bracket.

Parameters
----------
s : str
    A string with opening and closing brackets.

Returns
------
False : bool
    If a closing bracket has no corresponding opening bracket before it, it will return False.

check_stack.isEmpty : bool
    If the stack, where all the opening brackets have been placed on, still contain elements at the end of the string
    certain opening brackets had no corresponding opening bracket.

"""""
def is_correct_string(s):
    check_stack = mystack()
    for e in s:
        if e == '[' or e == '{' or e == '(' or e == '<':
            check_stack.push(e)
        if e == ']':
            if check_stack.peek() == '[':
                check_stack.pop()
            else:
                return False
        if e == '}':
            if check_stack.peek() == '{':
                check_stack.pop()
            else:
                return False
        if e == ')':
            if check_stack.peek() == '(':
                check_stack.pop()
            else:
                return False
        if e == '>':
            if check_stack.peek() == '<':
                check_stack.pop()
            else:
                return False
    return check_stack.isEmpty()

a = '[{(<>)}]'
print(is_correct_string(a))