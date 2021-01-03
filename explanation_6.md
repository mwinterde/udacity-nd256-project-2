**Complexity**
* The time complexity is for both operations O(n) since we need to loop
 through all elements of the two lists.
* The space complexity is O(n) since we do not further inflate the input data.


**Design Considerations** 
* For me, there was no alternative to looping through both lists. With this
 approach you then only need to keep track of some additional information
 while looping through the lists. For the union, we need to avoid duplicates. 
 Therefore I am using a set to keep track of values that have already been
 added to the result set. The same for the intersection. But in addition, I
 save all elements of the first list in another list, so that I can create
 the result set when looping through the second list.