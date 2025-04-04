from collections import deque

class stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)
    
def reverse_string(s):
    stk = stack()
    for char in s:
        stk.push(char)
        
    rev_str = ""
    while stk.size() != 0:
        rev_str += stk.pop()
    print(rev_str)        

def is_balanced(s):
    stk = stack()
    pairs = {')':'(', '}':'{', ']':'['}

    for char in s:
        if char in '({[':
            stk.push(char)
        elif char in ')}]':
            if stk.is_empty() or stk.pop() != pairs[char]:
                print('False')
                return False
            
    result = stk.is_empty()
    print(result)
    return result


if __name__ == '__main__':
    reverse_string("We will conquere COVI-19")
    reverse_string("I am the king")
    is_balanced(")HELLO( ]HELLO[") # --> False
    is_balanced("(HELLO) [HELLO]") # --> True
