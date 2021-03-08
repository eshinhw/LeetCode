class Solution:
    def myAtoi(self, s: str) -> int:

        if s == '':
            return 0

        # step1: removes leading whitespaces
        s = s.lstrip()

        digit = ''

        if '-' in s:
            s = s[s.index('-'):]
            digit = '' + '-'

        if '+' in s:
            s = s[s.index('+') + 1:]

        print(s)
        print(digit)

        print("=====")

        for i in range(len(s)):

            print(s[i])

            if s[i] == '-':
                continue

            if s[i].isdigit():
                digit = digit + s[i]

            if not s[i].isdigit():
                break

        print(digit)

        if digit.isdigit():
            output = int(digit)

            print(output)

            if output < -(2**31):
                return -(2**31)
            if output > (2**31) - 1:
                return (2**31) - 1

            return output
        else:
            return 0

Solution().myAtoi('42')