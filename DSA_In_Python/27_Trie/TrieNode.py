class TrieNode:
    def __init__(self):
        self.childs = {}
        self.isEnd = False

    @staticmethod
    def create(root, s):
        # root = TrieNode()
        temp = root
        for c in s:
            if c not in temp.childs:
                temp.childs[c] = TrieNode()
            temp = temp.childs[c]
        temp.isEnd = True
        return root