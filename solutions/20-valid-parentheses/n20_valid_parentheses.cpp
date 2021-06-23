#include <string>
#include <stack>

class Solution {
public:
    bool isValid(std::string s) {

        std::stack<char> stk;

        for (char p : s) {
            if (p == '(' || p == '{' || p == '[')
                stk.push(p);

            if (stk.empty())
                return false;

            if (p == ')') {
                char popped = stk.top();
                stk.pop();
                if (popped != '(')
                    return false;
            }
            if (p == '}') {
                char popped = stk.top();
                stk.pop();
                if (popped != '{')
                    return false;
            }
            if (p == ']') {
                char popped = stk.top();
                stk.pop();
                if (popped != '[')
                    return false;
            }
        }

        return stk.empty();

    }
};