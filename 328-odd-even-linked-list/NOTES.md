1.First keep two pointers for the starting nodes of odd-node and even-node respectively. I.e. odd = head; eHead = even = head.next.
2.Decide the while loop condition, which is the key point of this question.
- No matter what, when "even" exists (i.e. not None), "odd" exists. When there is even number of nodes, "even" will at a moment point to the last node of the linked list, which makes even.next is None. When there is odd number of nodes, "odd" will at a moment point to the last node, which means "even" points to None, i.e. odd.next.
- Considering the two scenarios above, we can have the while loop condition as even and even.next.
3.The content within the while loop is intuitive and after the while loop, we concatenate two list and return head.