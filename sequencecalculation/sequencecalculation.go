package main

import "fmt"

func main() {

	a := []int{10,1,6,8,9,15,19,21,54}
	b := []int{43,8,0,8,99,7,19,4,2}

	res := SmallestDifference(a, b)
	fmt.Println(res)
}


