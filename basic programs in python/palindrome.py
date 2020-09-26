class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        rev = 0
        output = False
        a = 2147483647
        b = -2147483648
        if x > 0:
            while x != 0:
                rem = x % 10
                x //= 10
                rev = rev * 10 + rem
                # print(rem, x, rev)
        if rev > a or rev < b:
            rev = 0
        if y == rev:
            output = True
        print(rev)
        return output


x = 21474836474
print(Solution().isPalindrome(x))