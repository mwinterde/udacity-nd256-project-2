**Complexity**
* The time complexity of all cache operations (`get()`, `set()` and `remove
()`) is O(1).
* The space complexity is O(n) as we create exactly one node per key. 
    
**Design Considerations**
* I have built the cache as a dictionary that saves nodes of a doubly linked
 list. The nodes store the (key, value) tuple for each key. Their order in
 the doubly linked list represent the access order of past cache operations. 
 Therefore we are able to remove the least recently used key from the
 cache if the specified capacity of the cache is reached.
* The challenge is to efficiently change the position of an existing key in the
 queue when it is called. In specific, to detach the existing node from its
 current position and put it to the tail. By storing the nodes in a
 dictionary we can avoid looping and therefore make it O(1).