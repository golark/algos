package main

import "log"


// binSearch returns index of the item in sequence, -1 if not found
func binSearch(seq []int, seek int) int {

	start := 0
	end := len(seq)

	for start < end {

		mid := ( end - start ) / 2 + start
		if seq[mid] == seek {
			return mid
		} else if seq[mid] > seek {
			end = mid
		} else {
			start = mid + 1
		}
	}

	return -1
}


func main() {

	seq := []int{0,5,6,7}

	log.Printf("seq %v | seek %v | index %v", seq, 5, binSearch(seq, 0))

}
