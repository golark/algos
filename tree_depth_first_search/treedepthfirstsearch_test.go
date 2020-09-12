package treedepthfirstsearch_test

import (
	treedepthfirstsearch "github.com/golark/algos/tree_depth_first_search"
	"testing"
)

const (
	succeed = "\u2713"
	failed  = "\u2717"
)

func TestMaxPathSum(t *testing.T) {

	head := treedepthfirstsearch.Tree{}
	l := treedepthfirstsearch.Tree {Data: 1}
	head.Left = &l
	r := treedepthfirstsearch.Tree{Data: 8}
	head.Right = &r

	t.Logf("Test:\twhen trying to find maxPathSum in binary Tree expecting %v", 8)

	res := treedepthfirstsearch.MaxPathSum(&head)
	if res != 8 {
		t.Fatalf("\t%s\texpected %v but received %v", failed, 8, res)
	}
	t.Logf("\t%s\tmax path sum match %v", succeed, res)
}
