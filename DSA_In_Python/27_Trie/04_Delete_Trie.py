from TrieNode import TrieNode


def deleteWord(root, s):
    def delete(temp, s, i):
        if i == len(s):
            if not temp.isEnd or len(temp.childs) != 0:
                return False
            return True

        c = s[i]
        if c not in temp.childs:
            return False
        
        if not delete(temp.childs[c], s, i+1):
            return False
        
        temp.childs.pop(c)
        return True
    
    return delete(root, s, 0), root

root = TrieNode()
TrieNode.create(root, "abdul")
TrieNode.create(root, "abdulhathi")
TrieNode.create(root, "hathi")

print(deleteWord(root, "abdul"))
isDelete, root = deleteWord(root, "hathi")
print(root)