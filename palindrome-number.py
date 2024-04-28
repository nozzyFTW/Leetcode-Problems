class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x == x.reverse() -> True
        # else -> False
        x_reversed = "".join(reversed(str(x)))
        if str(x) == x_reversed:
            return True
        else:
            return False