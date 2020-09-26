class Solution:
    def reverse(self, x):   # x - int
        rev = 0
        flag = 0
        a = 2147483647
        b = -2147483648
        if x < 0:
            x = -x
            flag = 1
        while x != 0:
            rem = x % 10
            x //= 10
            rev = rev * 10 + rem
            # print(rem, x, rev)
        if flag == 1:
            rev = -rev
        if rev > a or rev < b:
            rev = 0
        return rev


x = 120
y = Solution().reverse(x)
print(y)
