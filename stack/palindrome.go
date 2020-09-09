package main

import (
	"fmt"
	"github.com/golark/algo/stack"
)

// detectPalindrome
// stack based implementation
func detectPalindrome(s string) (bool, error) {

	// step 1 - traverse the runes and add to stack
	stck := stack.New()
	for _, r := range s {
		stck.Push(int(r))
	}

	// step 2 - pop stack to reverse
	var sRev string
	for ! stck.IsEmpty() {
		r, err := stck.Pop()
		if err != nil {
			return false, err
		}

		sRev += string(r)
	}

	// step 3 - check equality
	return sRev == s, nil
}

func main() {

	// test 1
	s1 := "abcdedfg"
	r, err := detectPalindrome(s1)
	if err != nil {
		fmt.Printf("%v", err)
		return
	}
	fmt.Printf("%v is a palindrome: %v\n", s1, r)

	// test 2
	s2 := "abcdcba"
	r, err = detectPalindrome(s2)
	if err != nil {
		fmt.Printf("%v", err)
		return
	}
	fmt.Printf("%v is a palindrome: %v\n", s2, r)
}
