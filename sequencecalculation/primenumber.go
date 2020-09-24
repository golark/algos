package main

import "fmt"

// isPrime
// return true if n is prime
func isPrime(n int) bool {

	if n <= 1 {
		return false
	} else if n == 2 {
		return true
	}

	if n%2 == 0 {
		return false
	}

	for i:=3; i< n; i=i+2 {
		if n%i == 0 {
			return false
		}
	}

	return true
}

// generatePrimeNumbers
// generate n prime numbers
func generateNPrimeNumbers(n int) []int {

	primeNums := make([]int, n)
	nextPrime := 1
	for i:=0; i<n; i++ {

		// find next prime number
		for isPrime(nextPrime) == false {
			nextPrime++
		}

		primeNums[i] = nextPrime
		nextPrime++
	}

	return primeNums
}

func main() {
	fmt.Printf("%v", generateNPrimeNumbers(10))
}
