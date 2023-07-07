from TrieNode import TrieNode

def searchWholeWord(root, s):
    temp = root
    for c in s:
        if c not in temp.childs:
            return False
        temp = temp.childs[c]
    return temp.isEnd


root = TrieNode()
TrieNode.create(root, "abdul")
print(searchWholeWord(root, "abdll"))