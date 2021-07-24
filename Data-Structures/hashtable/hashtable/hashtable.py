from hashtable.linked_list import LinkedList
# from linked_list import LinkedList
class Hashtable:
  def __init__ (self, size):
    self.size = size
    self.map = [None]*size
  def hash(self,key):
    sum = 0
    for chars in key:
      sum += ord(chars)
    sum *= 19
    index = sum % self.size
    return index
  
  def add(self, key, value):
    hashed_key = self.hash(key)
    if not self.map[hashed_key]:
      self.map[hashed_key] = LinkedList()
    if self.contains(key):
      return 'key already exists'

    self.map[hashed_key].add((key,value))

  def get(self,key):
    hashed_key = self.hash(key)
    if not self.map[hashed_key]:
      return None
    current = self.map[hashed_key].head
    while current:
      if current.data[0] == key:
        return current.data[1]
      current = current.next
    return None

  def contains(self,key):
    hashed_key = self.hash(key)
    if not self.map[hashed_key]:
      return False
    current = self.map[hashed_key].head
    while current:
      if current.data[0] == key:
        return True
      current = current.next
    return False



if __name__ == '__main__':
    hashtable = Hashtable(1024)
    hashtable.add('ahmad', 25)
    hashtable.add('hamad', 29)
    hashtable.add('silent', True)
    hashtable.add('listen', 'Hey man')
    print(hashtable.contains('ahmad'))