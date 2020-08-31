package twopointers

// two_numbers_target_sum
// given slice and target
// return true if 2 numbers sum up to the target
// O(n) time and O(n) space
func TwoNumberTargetSum(nums []int, target int) bool {

	// @todo: check if nums is empty

	// keep a dictionary of differences
	d := map[int]bool{}
	for _, v := range nums {
		if d[v] == true { // found a pair
			return true
		}
		diff := target - v
		d[diff] = true
	}

	return false
}
