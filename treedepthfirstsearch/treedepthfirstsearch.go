package treedepthfirstsearch

type Tree struct {
	Data int

	Left  *Tree
	Right *Tree
}

// branchSums
// return branch sums of binary Tree
// recursive approach
// O(n) space
func branchSums(node *Tree, sum int, s *[]int) {

	if node == nil {
		return
	}
	if node.Left == nil && node.Right == nil {
		sum += node.Data
		*s = append(*s, sum)
		return
	}

	sum += node.Data
	branchSums(node.Left, sum, s)
	branchSums(node.Right, sum, s)
}
