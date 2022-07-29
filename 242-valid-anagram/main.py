class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        td = {}
        sd = {}
        for sl, tl in zip(s, t):
            if sl == tl: continue
            
            if sl in td:
                if td[sl] == 1:
                    del td[sl]
                else:
                    td[sl] -= 1
            else:
                if sl in sd:
                    sd[sl] += 1
                else:
                    sd[sl] = 1
            
            if tl in sd:
                if sd[tl] == 1:
                    del sd[tl]
                else:
                    sd[tl] -= 1
            else:
                if tl in td:
                    td[tl] += 1
                else:
                    td[tl] = 1
        return not bool(td or sd)
