class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open = close = n
        res = []
        
        def genRecurse(open, close, str):
            if open == 0 and close == 0:
                res.append(str)
            elif open == 0:
                genRecurse(0, close - 1, str + ')')
            elif open == close:
                genRecurse(open - 1, close, str + '(')
            elif open < close:
                genRecurse(open - 1, close, str + '(')
                genRecurse(open, close - 1, str + ')')
        genRecurse(open, close, '')
        return res
