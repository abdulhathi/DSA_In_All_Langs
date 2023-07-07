from TrieNode import TrieNode

def insertTrie(s):
    root = TrieNode()
    temp = root
    for c in s:
        if c not in temp.childs:
            temp.childs[c] = TrieNode()
        temp = temp.childs[c]
    temp.isEnd = True
    return root

root = insertTrie("abdul")
print(root)