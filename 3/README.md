# Correct Solution Diagram
### Credit to https://leetcode.com/Google/

start = 0
max_length = 0
used_char = {} # This will map letters to numbers

Work Loop: for i in range(len(s))
Let s = abcabcbb
if s\[i\] in used_char and start <= used_char\[s\[i\]\]: start = used_char\[s\[i\]\] + 1
else: max_length = max(max_length, i - start + 1)

used_char\[s\[i\]\] = i

i = 0:
    a b c a b c b b
    ^
    i
    start = 0
    max_length = 0
    s\[i\] not in used_char, so max_length = max(0, 0 - 0 + 1), so max_length = 1
    used_char\[s\[i\]\] = i, so a : 0

i = 1:
    a b c a b c b b
      ^
      i
    start = 0
    max_length = 1
    s\[i\] not in used_char, so max_length = max(1, 1 - 0 + 1), so max_length = 2
    used_char\[s\[i\]\] = i, so used_char = { a:0, b:1 }

i = 3:
    a b c a b c b b
          ^
          i
    start = 0
    max_length = 3
    used_char = { a:0, b:1, c:2}
    used_char\[s\[i\]\] == 0
    s\[i\] in used_char and start <= 0, so start = 1
    used_char\[s\[i\]\] = i, so used_char = { b:1, c:2, a:3 }

i = 4:
    a b c a b c b b
            ^
            i
    start = 1
    max_length = 3
    used_char = { b:1, c:2, a:3 }
    used_char\[s\[i\]\] == 1
    s\[i\] in used_char and start <= 1, so start = 2
    used_char\[s\[i\]\] = i, so used_char = { c:2, a:3, b:4}

i = 6:
    a b c a b c b b
                ^
                i
    start = 3
    max_length = 3
    used_char = {a:3, b:4, c:5}
    used_char\[s\[i\]\] == 4
    s\[i\] in used_char and start <= 4, so start = 5
    used_char\[s\[i\]\] = i, so used_char = {  a:3, c:5, b:6}