'''
Given a string s, find the length of the longest substring without repeating characters.
'''


def lengthOfLongestSubstring(s: str) -> int:
    '''
    Strategy: Store all possible solutions, find the longest one
    '''
    bank = []
    i = 0
    for i in range(len(s)):
        temp = []
        while i < len(s) and s[i] not in temp:
            temp.append(s[i])
            i += 1
        bank.append(temp)
        
    print(bank)
    greatest = 0
    for sub in bank:
        greatest = max(greatest, len(sub))
    return greatest

def lengthOfLongestSubstringCORRECT(s):
    start = max_length = 0 
    usedChar = {} # Maps char : number
    
    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)

        usedChar[s[i]] = i

    return max_length