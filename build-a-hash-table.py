class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key_str:str):
        char_sum = 0
        for char in key_str:
            char_sum += ord(char)
        return hash(char_sum)

    def add(self, key, value):
        hkey = self.hash(key)
        if hkey in self.collection:
            self.collection[hkey][key] = value
        else:
            self.collection.update({hkey: 
            {key:value}})

    def remove(self, key):
        hkey = self.hash(key)
        if hkey in self.collection:
            self.collection[hkey].pop(key, None)
    
    def lookup(self, key):
        hkey = self.hash(key)
        if hkey in self.collection and key in self.collection[hkey]:
            return self.collection[hkey][key]
        else:
            return None

test_str = HashTable()
#print(test_str.hash("Test"))
test_str.add('fcc', 'me')
#print(test_str.collection)
#test_str.add('hell0', 'you')
#print(test_str.collection)
test_str.add('hell0', 'u')
print(test_str.collection)
print(test_str.lookup('cfc'))