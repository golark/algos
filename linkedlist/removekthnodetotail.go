package linkedlist

import (
	"fmt"
)

// RemoveKthNodeToTail
// remove k'th node before tail
// traverse through the linkedlist with 2 pointers to find k-1'th node
// then remove the node by manipulating the pointers
// O(n) time and O(1) space
func RemoveKthNodeToTail(head *node, K int) (*node, error) {

	// step 1 - check size is larger than K, cant remove K'th to last node
	size := Size(head)
	if K > size {
		return head, fmt.Errorf("K ( %v ) is larger than the size of the linkedlist %v, bailing", K, Size(head))
	} else if K-1 == size { // special case when trying to remove the head
		head = head.next
		return head, nil
	}

	// step 2 - find K-1'th to last node
	trailing := head
	node := head
	for i:=0;node.next!=nil;node=node.next{
		if i <= K {
			i += 1
			continue
		}
		trailing=trailing.next
	}
	nodeBeforeK := trailing

	// step 3 - remove node if it exists
	nodeBeforeK.next = nodeBeforeK.next.next

	return head, nil
}
