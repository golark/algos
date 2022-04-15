package main

import "log"

func countDigits(n int) int {

	numDigits := 0
	for n != 0 {
		numDigits++
		n /= 10
	}

	return numDigits
}


func main() {

	log.Printf("  1 | %v", countDigits(1))
	log.Printf(" 10 | %v", countDigits(10))
	log.Printf("100 | %v", countDigits(100))
}
