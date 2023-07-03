class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def validateParenthesis(s):
            st = []
            for c in s:
                if c == ')':
                    if not st:
                        return False
                    st.pop()
                    continue
                st.append(c)
            return st == []

        res = []
        def backtrack(s):
            if len(s) == (2*n):
                if validateParenthesis(s):
                    res.append(s)
                return
            backtrack(s+'(')
            backtrack(s+')')
        
        backtrack("")
        return res
    
print(Solution().generateParenthesis(3))


