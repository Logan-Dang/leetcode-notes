class Solution:
    def maximum69Number (self, num: int) -> int:
        i = 3
        track = big = num
        while i < num:
            if track % 10 == 6:
                big = num + i
            i *= 10
            track //= 10
        return big
