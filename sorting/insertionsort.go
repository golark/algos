package sorting

// findLargest
// returns the largest items index
func findLargest(s []int) int {

	idx := 0
	largest := s[0]
	for i,v := range s {
		if v > largest {
			largest = v
			idx = i
		}
	}

	return idx
}

// InsertionSort
// sorts in-place with InsertionSort algorithm
// 1. find largest
// 2. swap
func InsertionSort(s []int) {

	for i := range s {

		// step 1 - find largest
		idx := findLargest(s[i:])

		// step 2 - swap
		s[i], s[idx+i] = s[idx+i], s[i]
	}
}
