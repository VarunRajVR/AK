import random

class HashMap:
    def __init__(self, size=62):
        self.size = size
        self.map = [[] for _ in range(size)]
    
    def hash(self, key):
        sum=0
        for i in key:
            sum += ord(i)
        return sum % self.size
    
    def put(self, key, value):

        key_hash = self.hash(key)
        key_value = [key, value]   
        self.map[key_hash].append(key_value)
        return True

    def remove(self, key):
        key_hash = self.hash(key)
        for i in range(len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False


keys = []
for _ in range(100):
    key = str(random.randint(1, 10000))
    keys.append(key)


hash_map = HashMap()

#insert the keys
for i, key in enumerate(keys):
    hash_map.put(key, i)

#print hashmap
for index, bucket in enumerate(hash_map.map):
    print(f"Bucket {index}: {bucket}")