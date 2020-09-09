package main

import (
	"fmt"
	"github.com/golark/algo/stack"
)

// checkBalancedParanthesis
func checkBalancedParanthesis(s string) (bool, error) {

	stck := stack.New()

	// step 1 - traverse through the string and stack paranthesis
	for _, r := range s {
		if r == '(' || r == ')' {
			stck.Push(int(r))
		}
	}
	fmt.Printf("%v", stck)

	// step 2 - check if paranthesis are balanced by analysing the stack
	closeCount := 0
	openCount := 0
	for ! stck.IsEmpty() {

		i, err := stck.Pop()
		if err != nil {
			return false, err
		}

		if i == '(' {
			openCount++
		} else if i == ')' {
			closeCount++
		} else {
			return false, fmt.Errorf("unidentified rune in stack %v", i)
		}
	}

	return closeCount == openCount, nil
}


func main() {

	// test 1
	s := "(((())))"
	r, err := checkBalancedParanthesis(s)
	if err != nil {
		fmt.Printf("err occured %v", err)
		return
	}
	fmt.Printf("%v is balanced: %v\n", s, r)

	// test 2
	s = "()()(()"
	r, err = checkBalancedParanthesis(s)
	if err != nil {
		fmt.Printf("err occured %v", err)
		return
	}
	fmt.Printf("%v is balanced: %v\n", s, r)

}
