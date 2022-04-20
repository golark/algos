package sorting

import "log"

func insertionSort(seq []int) {

	// traverse sequence

	for i, _ := range seq {

		// sort i'th element
		idx := i
		for idx > 0 && seq[idx-1] > seq[idx] {
			seq[idx-1], seq[idx] = seq[idx], seq[idx-1]
			idx--
		}
	}
}


func main() {

	seq := []int{5,7,8,1,4,6}

	insertionSort(seq)

	log.Printf("%v", seq)
}