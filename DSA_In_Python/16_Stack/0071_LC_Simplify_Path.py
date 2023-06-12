class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        folders = path.split("/")
        for f in folders:
            if not f or f == ".":
                continue
            if f == "..":
                if st:
                    st.pop()
                continue
            st.append(f)
        # print(st)

        cPath = ""
        while st:
            cPath = "/" + st.pop() + cPath
        return "/" if cPath == "" else cPath

print(Solution().simplifyPath("/../"))
print(Solution().simplifyPath("/a/b///c/.././d/../f/"))


# path = "/a/b///c/.././d/../f/"
# print(path.split("/"))