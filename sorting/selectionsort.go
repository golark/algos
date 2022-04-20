package main

import "log"

// returns the minimum in given sequence
func minimumIndex(seq []int) int {

	min := seq[0]
	minIdx := 0
	for i, v := range seq {
		if v < min {
			min = v
			minIdx = i
		}
	}

	return minIdx
}

// selectionSort - sorts given sequence in place
func selectionSort(seq []int) {

	for i:=0; i<len(seq)-1; i++ {

		// find minimum on each iteration
		minIdx := minimumIndex(seq[i:])+i

		// place minimum to the correct slot in the sequence
		seq[minIdx], seq[i] = seq[i], seq[minIdx]
	}
}


func main() {
	seq := []int{5,6,1,2,6,2}
	selectionSort(seq)

	log.Printf("after %v", seq)
}
