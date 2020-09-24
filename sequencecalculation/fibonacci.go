package main

// fibonacci
// returns n'th number in fibonacci sequence
// 1st number is 0, 2nd number 1 etc...
func fibonacci(n int) int {

	if n == 1 {
		return 0
	} else if n == 2 {
		return 1
	}

	return fibonacci(n-1) + fibonacci(n-2)
}

func main() {
	
}
