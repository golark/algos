package treedepthfirstsearch

// max returns the max of 2 integers
func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// MaxPathSum
// wrapper around _maxPathSum
func MaxPathSum(head *Tree) int {
	return _maxPathSum(head, 0, 0)
}

// _maxPathSum
// returns the maximum path sum of a binary Tree
// depth first search, recursive approach
// O(n) time and O(1) space
func _maxPathSum(node *Tree, sum int, maxSum int) int {

	// return condition
	if node == nil {
		maxSum = max(sum, maxSum)
		return maxSum
	}
	if node.Left == nil && node.Right == nil {
		sum += node.Data

		maxSum = max(sum, maxSum)
		return maxSum
	}

	// recurse
	sum += node.Data
	return max(_maxPathSum(node.Right, sum, maxSum), _maxPathSum(node.Left, sum, maxSum))
}
