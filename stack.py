# # from collections import deque
# #
# # stack = deque()
# # stack.append('https//www.india.com')
# # stack.append('https//www.us.com')
# # stack.append('https//www.china.com')
# # stack.pop()
# # print(stack)
# #-----------------------------------------------------------------------------------------------
# # from collections import deque
# #
# # class stack:
# #     def __init__(self):
# #         self.container = deque()
# #
# #     def push(self,val):
# #         self.container.append(val)
# #
# #     def pop(self):
# #         self.container.pop()
# #
# #     def peek(self):
# #         return self.container[-1]
# #
# #     def is_empty(self):
# #         return len(self.container) == 0
# #
# #     def size(self):
# #         return len(self.container)
# #
# # s = stack()
# # s.push(5)
# # print(s.peek())
# # s.pop()
# #
# # print(s.is_empty())
# #
# # s.push(8)
# # s.push(45)
# # s.push(9)
# # print(s.peek())# always go last one till you not pop it
#
#
# #----------------------------------------------------------------------- Pratice ----------------------------------------------
#
# from collections import deque
#
# class Stack:
#     def __init__(self):
#         self.container = deque()
#
#     def push(self, val):
#         self.container.append(val)
#
#     def pop(self):
#         return self.container.pop()
#
#     def peek(self):
#         return self.container[-1]
#
#     def is_empty(self):
#         return len(self.container) == 0
#
#     def size(self):
#         return len(self.container)
#
# # def reverse_string(s):
# #     stack = Stack()
# #
# #     for ch in s:
# #         stack.push(ch)
# #
# #     rstr = ''
# #     while stack.size() != 0:
# #         rstr += stack.pop()
# #
# #     return rstr
#
# def reverse_string(s):
#     stack = Stack()
#     for ch in s:
#         stack.push(ch)
#
#     rstr = ''
#     while stack.size() != 0:
#         rstr += stack.pop()
#
#     return rstr
#
# if __name__ == '__main__':
#     print(reverse_string("We will conquere COVI-19"))
#     print(reverse_string("I am the king"))

#--------------------------------------------------Pratice--------------------------
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,value):
        self.container.append(value)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) ==0
    def size(self):
        return len(self.container)

def is_match(ch1,ch2):
    match_dict = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    return match_dict[ch1] == ch2
def is_balance(s):
    stack = Stack()
    for ch in s:
        if ch =='(' or ch ==')':
            stack.push(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if stack.size() == 0:
                return False
            if not is_match(ch,stack.pop()):
                return False
        return stack.size() == 0

if __name__ == '__main__':
    print(is_balance("({a+b})"))
    print(is_balance("))((a+b}{"))
    print(is_balance("((a+b))"))
    print(is_balance("((a+g))"))
    print(is_balance("))"))
    print(is_balance("[a+b]*(x+2y)*{gg+kk}"))