package twopointers

const UintSize = 32 << (^uint(0) >> 32 & 1) // 32 or 64

const (
	MaxInt  = 1<<(UintSize-1) - 1 // 1<<31 - 1 or 1<<63 - 1
	MinInt  = -MaxInt - 1         // -1 << 31 or -1 << 63
	MaxUint = 1<<UintSize - 1     // 1<<32 - 1 or 1<<64 - 1
)

// maxProfit
// returns the maximum profit
// given the prices
func MaxProfit(prices []int) int {

	minPrice := prices[0]
	mProfit := MinInt
	for _,v := range prices[1:] {
		profit := v - minPrice
		if profit > mProfit {
			mProfit = profit
		}

		if v < minPrice {
			minPrice = v
		}
	}

	return mProfit
}

