package twopointers

type item struct{
	id string
	value int
}

// knapsack
// find combination of 2 items that maximizes the value in the knapsack
// the total value of the knapsack must not exceed the capacity
// input slice is not sorted
// 2 pointers approach
// O(n^2) time and O(n) space
func knapsack(s []item, maxCapacity int) [][]item {

	smallestDiff := -32767
	res := make([][]item, 0)
	for i,_ := range s {
		for k := i;k<len(s);k++ {

			// check if we have a new max
			sum := s[i].value+s[k].value
			if sum <= maxCapacity  {
				if sum - maxCapacity > smallestDiff { // new max
					// remove previous entries and add current entry
					res = nil
					res = append(res, []item{s[i],s[k]})
				} else if sum-maxCapacity == smallestDiff {
					res = append(res, []item{s[i],s[k]})

				}
			}

		}
	}

	return res
}
