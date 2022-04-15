package main

import "log"

func factorialRecursive(n int) int {

	if n == 1 {
		return 1
	}

	return n * factorialRecursive(n-1)
}


func factorial(n int) int {

	fact := n
	for i:=n-1; i>0; i-- {
		fact *= i
	}

	return fact
}

func main() {

	log.Printf("%v", factorial(5))
	log.Printf("%v", factorialRecursive(5))
}
