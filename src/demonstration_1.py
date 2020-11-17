"""
Your task is create your own HashTable without using a built-in library.
​
Your HashTable needs to have the following functions:
​
- put(key, value) : Inserts a (key, value) pair into the HashTable. If the
value already exists in the HashTable, update the value.
- get(key): Returns the value to which the specified key is mapped, or -1 if
this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key if this map contains the
mapping for the key.
​
Example:
​
```plaintext
hash_table = MyHashTable();
hash_table.put("a", 1);
hash_table.put("b", 2);
hash_table.get("a");            // returns 1
hash_table.get("c");            // returns -1 (not found)
hash_table.put("b", 1);         // update the existing value
hash_table.get("b");            // returns 1
hash_table.remove("b");         // remove the mapping for 2
hash_table.get("b");            // returns -1 (not found)
```
"""
​
# Used for when we implement linked list chaining to handle collisions 
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
​
class MyHashTable:
    def __init__(self, capacity=100):
        # Your code here
        self.capacity = capacity
        # initializing an array of None values that has length of `capacity` 
        self.storage = [None for _ in range(self.capacity)]
​
    # returns an integer output that will be used to index into `self.storage` 
    def _hash(self, input):
        hash = id(input)
        # we have to ensure that `hash` is within bounds of our storage 
        return hash % self.capacity
​
    def put(self, key, value):
        # Your code here
        # 1. hash our key to figure out where in storage this key-value will go 
        index = self._hash(key) 
        # 2. once we know the index, check that that spot is available 
        if self.storage[index] is None:
        # 3. if it is, insert the key-value pair at that spot 
            self.storage[index] = ListNode(key, value)
        # otherwise, update the key-value pair at that spot 
        else:
            # there's already a linked list at this array slot 
            # to add this key-value pair, we need to traverse the linked list 
            # to get to the end, and then add the key-value pair to the tail 
            # of our linked list 
            current = self.storage[index]
            # if we get to the end of the linked list, that means we never 
            # saw a matching key in the linked list, so we'll go ahead and 
            # add a new node to the end of this linked list 
            while current is not None:
                # while traversing our linked list, check each node's key 
                # to see if it matches the input key 
                # if it does, we need to overwrite that key's value instead 
                # of inserting a new linked list node 
                if current.key == key:
                    current.value = value
                    return 
                # check if current.next is None
                # if it is, add the new list node after current 
                if current.next is None:
                    current.next = ListNode(key, value)
                    return 
                current = current.next
​
    def get(self, key):
        # Your code here
        # 1. hash our key to figure out the spot where this key-value pair will
        # be in our storage 
        index = self._hash(key) 
        # 2. check the index in self.storage to make sure that the key-value pair 
        # actually exists at that spot 
        if self.storage[index] is not None:
            # traverse the linked list to try and find the key that matches the
            # input key 
            current = self.storage[index]
            while current is not None:
                if current.key == key:
                    return current.value
                current = current.next
            # if we get to the end of the linked list, then no node's matched 
            # the key we were looking for 
        return -1 
​
    def remove(self, key: int) -> None:
        # Your code here
        # 1. hash our key to figure out the spot where this key-value pair will 
        # be in our storage 
        index = self._hash(key)
        # 2. check the index in self.storage to make sure that the key-value pair 
        # actually exists at that spot 
        if self.storage[index] is not None:
            current = self.storage[index]
            prev = None 
            while current is not None:
                if current.key == key:
                    # check if prev is None 
                    # if prev is None, that means that the first linked list node 
                    # holding the key we're looking to remove 
                    # set self.storage[index] = current.next 
                    if prev is None:
                        self.storage[index] = current.next 
                        return 
                    # set prev.next = current's next 
                    prev.next = current.next 
                    prev = current 
                    current = current.next 
            
​
hash_table = MyHashTable()
hash_table.put("a", 1)
hash_table.put("b", 2)
print(hash_table.get("b"))
print(hash_table.get("a"))         
print(hash_table.get("c"))          
hash_table.put("b", 1)         
print(hash_table.get("b"))           
hash_table.remove("b")        
print(hash_table.get("b"))