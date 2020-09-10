package sorting

import "fmt"

/*
- choose a pivot
- create right/left references
- move left  reference towards middle until encountered an item larger  than pivot
- move right reference towards middle until encountered an item smaller than pivot
- swap right and left references
- move the pivot to the middle
- iterate until single element is left
 */
func QuickSort(q []int) {

	quickSortRecursive(q, 0, len(q)-1)

}

func quickSortRecursive(q []int, left int, right int) {


	if left >= right {
		return
	}

	end := right
	start := left
	fmt.Printf("%v\n", q[start:end])
	pivot  := q[end]
	right--

	midIdx := (end - start) /2

	for right > left {

		if q[right] > pivot {
			right--
		}
		if q[left] < pivot {
			left++
		}

		if q[left] > pivot && q[right] < pivot {
			q[left], q[right] = q[right], q[left]
			right--
			left++
		}
	}
	q[midIdx],q[end] = q[end], q[midIdx] // place the pivot in the middle

	fmt.Printf("%v\n\n", q[start:end])
	quickSortRecursive(q, start, (end-1)/2)
	quickSortRecursive(q, (end+1)/2, end)
}
