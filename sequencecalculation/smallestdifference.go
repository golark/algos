package main

import (
	"sort"
)

func Abs(x int) int{
	if x < 0 {
		return -x
	}
	return x
}

func Min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}


// smallestDifference
// find smallest difference between 2 unsorted slices
// first sort the arrays
// traverse through the slices, keeping a minimum difference
// each iteration move the smaller items pointer
func SmallestDifference(a []int, b []int) int {

	// @todo: check length of the slices

	// step 1 - sort
	sort.Ints(a)
	sort.Ints(b)

	// step 2 - traverse through, keeping minimum distance
	q := 0
	p := 0
	minDiff := Abs(a[0] - b[0])
	for ; p<len(a)-1 || q<len(b)-1; {

		if (b[q] < a[p] && q < len(b)-1) || p == len(a)-1 {
			q += 1
		} else {
			p += 1
		}

		diff := Abs(a[p] - b[q])
		minDiff = Min(minDiff, diff)
	}

	return minDiff
}


