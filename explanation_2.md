**Complexity**
* The time complexity is O(n) since we loop through each file beneath path
 exactly once.
* The space complexity is also O(n) since in the worst case scenario (all
 files beneath path have the specified suffix) we would return a list of
 length n.
    
**Design Considerations**
* This is a typical use case for recursion. We need to walk through all
 subdirectories beneath path and scan each file in these subdirectories. I
 think there is no chance to avoid that and so recursion is a plausible
 approach to make this O(n).