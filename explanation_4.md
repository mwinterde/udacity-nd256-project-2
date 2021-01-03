**Complexity**
* The time complexity is O(n) since in the worst case we need to loop
 through all members of a specific group.
* The space complexity is also O(n) since we work with arrays that contain
 all members.


**Design Considerations** 
* I again came up with a recursive function to solve the problem. The
 major challenge of the given problem is to deal with the nesting of groups
 since in the worst case the group structure could have hundreds of levels. 
 To deal with this structure, recursion is a very good approach.