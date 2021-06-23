from typing import List

class Solution:


    def _helper(self, substring: str):

        sub_list = []

        if substring[0] == '0' and substring[len(substring)-1] == '0':
            sub_list.append('0')
            return sub_list

        # start with 0: 012
        if substring[0] == '0':
            new_string = substring[0] + '.' + substring[1:]
            sub_list.append(new_string)
            return sub_list

        if substring[len(sub_list) - 1] == '0':
            sub_list.append(substring)
            return sub_list

        sub_list.append(substring)

        for i in range(1,len(substring)):
            new_string = substring[0:i] + '.' + substring[i:]
            sub_list.append(new_string)

        return sub_list

    def ambiguousCoordinates(self, s: str) -> List[str]:
        # remove parentheses
        s = s[1:len(s)-1]
        print(s)

        out_list = []

        for i in range(1,len(s)):

            left = self._helper(s[0:i])
            right = self._helper(s[i:])

            for l in left:

                for r in right:

                    out_list.append("(" + l + ", " + r + ")")

        print(out_list)
        return out_list


sol = Solution()
sol.ambiguousCoordinates('(00011)')