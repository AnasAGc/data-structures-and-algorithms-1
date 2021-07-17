
from linked_list import LinkedList
class Hashtable:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size
    
    def hash(self, key):
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp_value = sum_of_asccii * 19
        hashed_key = temp_value % self.size
        return hashed_key
    
    def add(self, key, value):
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = LinkedList()
        else:
            if self.contains(key):
                return 'key already exists'
        self.map[hashed_key].add((key,value))
    
    def contains(self,key):
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            return False # False means does not exist
        else:
            temp = self.map[hashed_key].values()
            for subarrays in temp:
                if subarrays[0] == key:
                    return True
            return False
    def get(self,key):
        hashed_key = self.hash(key)
        if not self.contains(key):
            return None
        temp = self.map[hashed_key].values()
        for subarrays in temp:
            if subarrays[0] == key:
                return subarrays[1]





if __name__ == '__main__':
    hashtable = Hashtable(1024)
    hashtable.add('ahmad', 25)
    hashtable.add('hamad', 29)
    hashtable.add('silent', True)
    hashtable.add('listen', 'Hey man')
    print(hashtable.contains('ahmad'))