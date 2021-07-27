# from hashtable.linked_list import LinkedList
from linked_list import LinkedList
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


import string
def repeated_word(str):
    str = str.translate(str.maketrans('', '', string.punctuation))
    words = str.split()
    hashmap = Hashtable(len(words))
    for word in words:
      if hashmap.contains(word.lower()):
        return word
      hashmap.add(word.lower(),1)
    return None


if __name__ == '__main__':
    hashtable = Hashtable(1024)
    hashtable.add('ahmad', 25)
    hashtable.add('hamad', 29)
    hashtable.add('silent', True)
    hashtable.add('listen', 'Hey man')
    # print(hashtable.contains('ahmad'))
    print(repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."))
    print(repeated_word("Once upon a time, there was a brave princess who..."))
    print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))