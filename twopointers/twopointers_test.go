package twopointers_test

import (
	twopointers "github.com/golark/algos/twopointers"
	log "github.com/sirupsen/logrus"
	"testing"
)

const (
	succeed = "\u2713"
	failed  = "\u2717"
)

func init() {
	log.SetLevel(log.PanicLevel) // do not log during testing below panic
}

func Test_MaxProfit(t *testing.T) {

	prices := []int{10,5,2,1,0,-1,10,50,60}

	t.Logf("Test:\twhen trying find max profit in prices %v checking for max profit of %v", prices, 61)
	profit := twopointers.MaxProfit(prices)

	if profit != 61 {
		t.Fatalf("\t%s\tshould return %v but returned %v", failed, 61, profit)
	}
	t.Logf("\t%s\tshould return %v",succeed, profit)
}

func Test_twoNumberTargetSum(t *testing.T) {

	nums := []int{10,5,2,1,0,-1,10,50,60}

	t.Logf("Test:\twhen trying find if 2 numbers in %v sum up to %v", nums, 11)
	res := twopointers.TwoNumberTargetSum(nums, 11)

	if res != true {
		t.Fatalf("\t%s\tshouldn't return %v", failed, res)
	}
	t.Logf("\t%s\tshould return %v",succeed, res)
}

func Test_IsPalindrome(t *testing.T) {

	s := "abbaabba"

	t.Logf("Test:\twhen trying chec if %v is a palindrome", s)
	res := twopointers.IsPalindrome(s)

	if res != true {
		t.Fatalf("\t%s\tshouldn't return %v", failed, res)
	}
	t.Logf("\t%s\tshould return %v",succeed, res)


	s = "abcdefgh"

	t.Logf("Test:\twhen trying chec if %v is a palindrome", s)
	res = twopointers.IsPalindrome(s)

	if res != false {
		t.Fatalf("\t%s\tshouldn't return %v", failed, res)
	}
	t.Logf("\t%s\tshould return %v",succeed, res)
}

func Test_MinimumWindowSort(t *testing.T) {

	s := []int{4, 5, 1, 10, 11, 12, 14, 5, 20}

	t.Logf("Test:\twhen trying to find unsorted section of %v", s)
	res := twopointers.MinimumWindowSort(s)

	if len(res) != 6 {
		t.Fatalf("\t%s\tshouldn't return %v", failed, res)
	}
	t.Logf("\t%s\tshould return %v", succeed, res)

}
