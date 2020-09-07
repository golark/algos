package main

import "fmt"

type tree struct {
	data int

	left *tree
	right *tree
}

// branchSums
// return branch sums of binary tree
// recursive approach
// O(n) space
func branchSums(node *tree, sum int, s *[]int) {

	if node == nil {
		return
	}
	if node.left == nil && node.right == nil {
		sum += node.data
		*s = append(*s, sum)
		return
	}

	sum += node.data
	branchSums(node.left, sum, s)
	branchSums(node.right, sum, s)
}

func main() {

	head := tree{0, nil, nil}
	l := tree {1, nil, nil}
	head.left = &l
	r := tree {2, nil, nil}
	head.right = &r

	s := make([]int, 0)
	s = append(s, 9)
	branchSums(&head, 0, &s)

	fmt.Println(s)

	
}
