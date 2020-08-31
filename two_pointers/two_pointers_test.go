package twopointers_test

import (
	twopointers "github.com/golark/algos/two_pointers"
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
