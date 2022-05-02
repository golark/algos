package main

import "log"

// mergeSort accepts slice of integers, sorts in place using merge sorting
// recursive implementation
func mergeSort(seq []int) []int {

	if len(seq) < 2 {
		return seq
	}

	first := mergeSort(seq[:len(seq)/2]) // lhs
	second := mergeSort(seq[len(seq)/2:]) // rhs

	log.Printf("first %v | second %v", first, second)

	return merge(first, second)
}

// innerSort sorts two lists using two pointer sort
// @todo: explanation of two pointer sort
func merge(first []int, second []int) []int {

	var merged []int
	a := 0
	b := 0

	for ; a< len(first) && b<len(second); {
		if first[a] > second[b] {
			merged = append(merged, first[a])
			a++
		} else {
			merged = append(merged, second[b])
			b++
		}
	}

	for ; a < len(first); a++ {
		merged = append(merged, first[a])
	}
	for ; b < len(second); b++ {
		merged = append(merged, second[b])
	}

	return merged
}

func main() {
	seq := []int{4,5,6,7,1,2,4,1,8,9,10,11,111,2312,632}

	sorted := mergeSort(seq)
	log.Printf("%v", sorted)

}
