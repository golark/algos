package main

import "fmt"

func sDifference(a,b  []int) int {

	smallestDiff := a[0] - b[0]
	for _, x := range a[1:] {
		for _, y := range b {
			if x-y < smallestDiff {
				smallestDiff = x-y
			}

		}
	}

	return smallestDiff
}


func main() {

	a := []int{10,1,6,8,9,15,19,21,54}
	b := []int{43,8,0,8,99,7,19,4,2}

//	res := SmallestDifference(a, b)
	res := sDifference(a, b)
	fmt.Println(res)
}


