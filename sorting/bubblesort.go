package sorting

// BubbleSort
// in place Bubble sort algorithm
// compare every 2 elements
// larger moves up ( like bubbles up water )
// iterate through len(s) - 1 times
func BubbleSort(s []int) {

	for i:=0;i<len(s)-1;i++ {

		for j:=0;j<len(s)-1;j++ {
			// bubble up
			if s[j+1] > s[j] {
				s[j], s[j+1] = s[j+1], s[j]
			}
		}
	}

}
