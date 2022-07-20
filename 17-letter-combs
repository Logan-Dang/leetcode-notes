class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def letterRecurse(digits):
            if not digits: return ['']
            res = []
            for char in letters[digits[0]]:
                for sub in letterRecurse(digits[1:]):
                    res.append(char + sub)
            return res
        
        if not digits: return None
        return letterRecurse(digits)
                
                
        
