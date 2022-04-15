package main

func numDigits(n int) int {

	cnt := 0
	for n != 0 {
		n = n % 10
		cnt++
	}

	return cnt
}

func isArmstrong(n int) bool {
	return false
}


func main() {
	n := numDigits(1567)
	print(n)
}
