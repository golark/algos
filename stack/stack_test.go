package stack_test

import (
	"github.com/golark/algos/stack"
	"testing"
)

const (
	succeed = "\u2713"
	failed  = "\u2717"
)

func init() {
}

func TestPopEmptyStack(t *testing.T) {

	t.Logf("Test:\twhen trying to pop from empty stack expecting error")

	s := stack.New()
	_, err := s.Pop()

	if err == nil {
		t.Fatalf("\t%s\tshould return error %v", failed, err)
	}
	t.Logf("\t%s\tshould return error: %v", succeed, err)
}

func TestPushStack(t *testing.T) {

	items := []int{1,2,3,4}
	exp   := []int{4,3,2,1}
	t.Logf("Test:\twhen trying to push items %v to stack, waiting for popping in reverse %v", items, exp)

	// push items
	s := stack.New()
	for _,v := range(items) {
		s.Push(v)
	}

	// pop items
	var out []int
	for _ = range exp {
		i, err := s.Pop()

		if err != nil {
			t.Fatalf("\t%s\tshouldn't return error while popping: %v", failed, err)
		}
		out = append(out, i)
	}


	for i := range exp {
		if exp[i] != out[i] {
			t.Fatalf("\t%s\tmismatching items %v %v", failed, exp, out)
		}
	}
	t.Logf("\t%s\titems match: %v", succeed, out)
}

