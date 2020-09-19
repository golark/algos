package linkedlist

import "fmt"

type node struct {
	data interface{}
	next *node
}

// NewLinkedList
// factory function
func NewLinkedList(data []interface{}) *node {

	if len(data) == 0 {
		return nil
	}

	head := node{data[0], nil}
	pNode := &head
	for _,v := range data[1:] {
		newNode := node{v, nil}
		pNode.next = &newNode
		pNode = pNode.next
	}

	return &head
}

// Size
// returns the Size of the linkedlist
// O(n) time, O(1) space
func Size(head *node) int {

	n := 0
	node := head
	for ;node != nil; node=node.next{
		n += 1
	}

	return  n
}

// Display
// display linked list contents
func Display(head *node) {

	// print head -> tail but omit tail
	p := head
	for ;p.next!=nil;p=p.next{
		fmt.Printf("%v -> ", p.data)
	}
	fmt.Printf("%v\n", p.data)

}

// Reverse
// inplace reversal
// traverse through one time and reverse
// returns new head
// O(n) time, O(1) space
func Reverse(head *node) *node {

	if head == nil {
		return nil
	}

	var p *node
	n := head
	for ;n.next != nil; {
		t := n.next // save next temporarily
		n.next = p  // reverse pointer
		p,n = n,t
	}

	// handle tail
	n.next = p
	return n
}
