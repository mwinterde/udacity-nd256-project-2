**Complexity**
* The time complexity of the encoding is O(n^2) in the worst case. 
    * Counting the frequency of letters is O(n). 
    * But creating the priority queue is O(n^2) since we loop through each
     letter which is in worst case O(n) and need to make an insertion at the
     right position in the priority queue which is in worst case also O(n).
    * The derivation of letter codes from the Huffman Tree is O(n) in the
     worst case, depending on the specific letter frequencies.
* The time complexity of the decoding is O(n) since we simply loop over the
 encoded string.
* The space complexity of both the encoding and decoding is O(n).
    
**Design Considerations** 
* The major challenge was the design of the priority queue. I needed a data
 structure that would allow me to implement the tree building process of the
 Huffman encoding. Since we need some form of a priority queue anyway, I
 came up with the idea, to store the tree nodes for the Huffman tree in the
 data attribute of the queue nodes. By doing so, it becomes very easy to
 implement the tree building.
* For the derivation of the letter codes from the tree I have come up with a
 recursive function that traverses to the leaf nodes of the tree and keeps
 track of the specific path to that leaf node in a string (for each left
  traversal we append "0", for right traversal we append "1").
* Once you have the encoding, the decoding is relatively straightforward. We
 loop through the encoded string and in each iteration we make one move in the
 Huffman tree (again "0" = left, "1" = right). Always when we reach a leaf
 node we append the corresponding letter to the result set and restart from
 the head of the tree.