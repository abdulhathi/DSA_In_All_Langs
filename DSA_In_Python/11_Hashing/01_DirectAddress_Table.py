class DirectAddress:
    def __init__(self, size):
        self.ht = [0] * size

    def insert(self, key):
        if self.ht[key] != 0:
            return False
        self.ht[key] = 1
        return True
    
    def delete(self, key):
        if self.ht[key] == 0:
            return False
        self.ht[key] = 0
        return True
    
    def search(self, key):
        return self.ht[key] == 1
    
directAddress = DirectAddress(100)
print(directAddress.insert(1))
print(directAddress.insert(10))
print(directAddress.search(10))
print(directAddress.search(50))
print(directAddress.delete(51))
print(directAddress.delete(10))