**Complexity**
* The time complexity of adding an element to the blockchain is O(1
). Printing the blockchain takes O(n).
* The space complexity is O(n) in both cases since do not use more than the
 input data.


**Design Considerations** 
* Since the specific requirements were not so obvious for this case, I
 decided to come up with a simple blockchain that has two functionalities: 1) 
 You can add new blocks to the blockchain. Since we always keep track of the
 latest block of the chain this operation is very efficient. I thought that
 efficiency is most important at this point as it is the major functionality
 of the blockchain. 2) You can print the full history of the blockchain. In
 order to be able to search through the history of the blockchain, I came up
 with a dictionary that stores all blocks of the blockchain together with their
 corresponding hash code. Starting from the head, and using the
 previous_hash attribute of each block, we can then loop backwards to the
 first block of the blockchain.