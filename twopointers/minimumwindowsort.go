package twopointers

// mimimumwindowsort
// find minumum window when sorted will sort the whole slice
// two pointers approach
// O(n) time and O(1) space
func MinimumWindowSort(s []int) []int {

	if len(s) == 0 {
		return make([]int, 0)
	}

	p := 0
	q := len(s)-1
	for ;p < q; {

		if s[p] > s[p+1] && s[q] < s[q-1] {
			break
		}
		if s[p] < s[p+1] {
			p += 1
		}
		if s[q] > s[q-1] {
			q -= 1
		}
	}

	return s[p+1:q+1]
}
