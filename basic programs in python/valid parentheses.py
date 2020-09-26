class Solution:
    def isValid(self, s: str) -> bool:
        mylist = []
        # print(len(s))
        for i in s:
            if i == "(" or i == "[" or i == "{":
                mylist.append(i)
                # print(mylist)
                # continue

            # print(mylist)
            if len(mylist) == 0:
                return False

            if i == ")":
                x = mylist.pop()
                # print(x)
                if x == "[" or x == "{":
                    return False
            elif i == "}":
                x = mylist.pop()
                # print(x)
                if x == "[" or x == "(":
                    return False
            elif i == "]":
                x = mylist.pop()
                # print(x)
                if x == "(" or x == "{":
                    return False

        if len(mylist) == 0:
            return True
        else:
            return False


expr = "{()}[]"
valid = Solution().isValid(expr)
print(valid)