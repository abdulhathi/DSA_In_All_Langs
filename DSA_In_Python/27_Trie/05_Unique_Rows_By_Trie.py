from TrieNode import TrieNode

def countUniqueRows(matrix):
    root = TrieNode()
    def insert(row):
        temp = root
        for val in row:
            if val not in temp.childs:
                temp.childs[val] = TrieNode()
            temp = temp.childs[val]
        temp.isEnd = True
    
    def search(row):
        temp = root
        for val in row:
            if val not in temp.childs:
                return False
            temp = temp.childs[val]
        return temp.isEnd

    count = 0
    for row in matrix:
        if not search(row):
            insert(row)
            continue
        count += 1
    return count

matrix = [[1,0,0],[1,1,1],[1,0,0],[1,1,1]]
matrix = [[1,0,0],[1,0,0]]
print(countUniqueRows(matrix))