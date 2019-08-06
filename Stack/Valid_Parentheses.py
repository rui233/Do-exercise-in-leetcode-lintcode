# Description:
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:

# 1.Open brackets must be closed by the same type of brackets.
# 2.Open brackets must be closed in the correct order.
#
#
#
#Solution1:
class Solution:
    def isValid(self, s):
        stack = []
        paren_map = {')': '(', '}': '{', ']': '['}#python中内置的字典dict在其它语言中叫做map
        for c in s:
            if c not in paren_map:
                stack.append(c)
            elif not stack or paren_map[c] != stack.pop:
                return False
        return not stack


#class Solution2:
class Solution2(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        dic = {')':'(', '}':'{', ']':'['} # 括号的map
        for c in s:
            if c == '(' or c == '[' or c == '{':# 左括号
                st.append(c)
            elif c == ']' or c == ')' or c == '}':# 右括号
                if len(st) == 0 or st.pop() != dic[c]: # 栈为空或者栈顶不匹配，返回false
                    return False
        return len(st) == 0