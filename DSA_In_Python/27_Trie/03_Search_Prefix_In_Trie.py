from TrieNode import TrieNode

def prefixSearch(root, prefix):
    temp = root
    for c in prefix:
        if c not in temp.childs:
            return False
        temp = temp.childs[c]
    return True

root = TrieNode()
TrieNode.create(root, "abdulhathi")
print(prefixSearch(root, "hathi"))
print(prefixSearch(root, "abdul"))