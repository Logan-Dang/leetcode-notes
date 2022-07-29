class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def matches(word, pattern):
            w = p = None
            wd = {}
            pset = set()
            for i in range(len(word)):
                if word[i] != w and pattern[i] != p:
                    if word[i] in wd:
                        if wd[word[i]] != pattern[i]:
                            return False
                    elif pattern[i] in pset: return False
                    wd[w] = p
                    pset.add(p)
                    w = word[i]
                    p = pattern[i]
                elif word[i] != w or pattern[i] != p:
                    return False
            return True
        
        res = []
        for word in words:
            if matches(word, pattern):
                res.append(word)
        return res
    
    def findNormalize(self, words, p):
        def F(w):
            m = {}
            return [m.setdefault(c, len(m)) for c in w]
        return [w for w in words if F(w) == F(p)]
    
    def findIso
        b = pattern
        def is_iso(a):
            return len(a) == len(b) and len(set(a)) == len(set(b)) == len(set(zip(a, b)))
        return filter(is_iso, words)
