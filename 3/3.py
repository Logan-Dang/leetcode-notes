'''
Given a string s, find the length of the longest substring without repeating characters.
'''


def lengthOfLongestSubstringLOGAN(s: str) -> int:
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
    '''
    Credit to: https://leetcode.com/Google/
    '''
    start = max_length = 0 
    used_char = {} # Maps char : number
    
    for i in range(len(s)):
        if s[i] in used_char and start <= used_char[s[i]]: # check if the current substring has a repeating character, then check if the head
            # of the current substring is less than or equal to the index of last repeated character, the second check is important
            # because we don't clear the dictionary and don't want to be stopped by an old repeated character
            start = used_char[s[i]] + 1 # set the new head to the chatacter after
        else:
            max_length = max(max_length, i - start + 1) # the solution is either the current solution or 
            # the distance between the pointer and the start of the current substring + 1 (the length of the substring)

        used_char[s[i]] = i

    return max_length