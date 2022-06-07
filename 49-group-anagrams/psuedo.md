### My solution

```python
# O(n^2 lgn) solution
function groupAnagram(strs: List):
    bank = {}
    for each word in strs:
        sort = sorted(list(word))
        if sort in bank.keys:
            bank[sort].append(word)
        else
            bank[sort] = [word]

    result = []
    for key, value in bank.items():
        result.append(value)
```

