package sorting_test

import (
	sorting "github.com/golark/goindepth/sorting"
	log "github.com/sirupsen/logrus"
	"reflect"
	"testing"
)

const (
	succeed = "\u2713"
	failed  = "\u2717"
)

func init() {
	log.SetLevel(log.PanicLevel) // do not log during testing below panic
}

func TestInsertSort(t *testing.T) {

	testCases := [][]int {
		{1,2,3,4,5,6,7,8,9,10},
		{10,9,8,7,6,5,4,3,2,1},
	}
	expected := [][]int {
		{10,9,8,7,6,5,4,3,2,1},
		{10,9,8,7,6,5,4,3,2,1},
	}

	textIdx := 0
	for i := range testCases {
		r := testCases[i]

		t.Logf("Test %v:\twhen trying to Insert sort %v, checking for %v",i, r, expected[i])
		sorting.InsertionSort(r)

		if ! reflect.DeepEqual(r, expected[i]) {
			t.Fatalf("\t%s\tshould return %v but returned %v", failed, expected[i], r)
		}
		t.Logf("\t%s\tshould return %v", succeed, expected[i])

		textIdx++
	}
}

func TestBubbleSort(t *testing.T) {

	testCases := [][]int {
		{1,2,3,4,5,6,7,8,9,10},
		{10,9,8,7,6,5,4,3,2,1},
	}
	expected := [][]int {
		{10,9,8,7,6,5,4,3,2,1},
		{10,9,8,7,6,5,4,3,2,1},
	}

	textIdx := 0
	for i := range testCases {
		r := testCases[i]

		t.Logf("Test %v:\twhen trying to Bubble sort %v, checking for %v",i, r, expected[i])
		sorting.BubbleSort(r)

		if ! reflect.DeepEqual(r, expected[i]) {
			t.Fatalf("\t%s\tshould return %v but returned %v", failed, expected[i], r)
		}
		t.Logf("\t%s\tshould return %v", succeed, expected[i])

		textIdx++
	}
}

func TestQuickSort(t *testing.T) {

	testCases := [][]int {
		{2,10,3,6,9,5,7,1,8,4},
		{10,9,8,7,6,5,4,3,2,1},
	}
	expected := [][]int {
		{1,2,3,4,5,6,7,8,9,10},
		{1,2,3,4,5,6,7,8,9,10},
	}

	textIdx := 0
	for i := range testCases {
		r := testCases[i]

		t.Logf("Test %v:\twhen trying to Insert sort %v, checking for %v",i, r, expected[i])
		sorting.QuickSort(r)

		if ! reflect.DeepEqual(r, expected[i]) {
			t.Fatalf("\t%s\tshould return %v but returned %v", failed, expected[i], r)
		}
		t.Logf("\t%s\tshould return %v", succeed, expected[i])

		textIdx++
	}
}

