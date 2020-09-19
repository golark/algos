package linkedlist_test

import (
	"github.com/golark/algos/linkedlist"
	"testing"
)

const (
	succeed = "\u2713"
	failed  = "\u2717"
)

func Test_LinkedListSize(t *testing.T) {

	data := []interface{}{1,2,3,4,5}
	head := linkedlist.NewLinkedList(data)
	linkedlist.Display(head)

	t.Logf("Test:\twhen trying to check the size of a linkedlist expecting %v",5)
	size := linkedlist.Size(head)

	if size != 5 {
		t.Fatalf("\t%s\tshould return %v but returned %v", failed, 5, size)
	}
	t.Logf("\t%s\tshould return %v",succeed, size)

}

func Test_RemoteKthToLastNode(t *testing.T) {

}


