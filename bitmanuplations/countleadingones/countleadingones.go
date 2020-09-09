package main

import (
	"fmt"
	"unsafe"
)

func cntLeadZeros(n uint) uint {

	cnt := unsafe.Sizeof(n) * 8  - 1

	for ( ( n >> cnt ) & 0x1 ) != 1 {
		cnt--
	}

	return uint(unsafe.Sizeof(n)*8)-1 - uint(cnt)
}

func cntLeadOnes(n uint) uint {

	cnt := unsafe.Sizeof(n) * 8  - 1

	for ( ( n >> cnt ) & 0x1 ) == 1 {
		cnt--
	}

	return uint(unsafe.Sizeof(n)*8)-1 - uint(cnt)
}


func main() {
	fmt.Printf("0x%x leading zeros = %v\n\n", 0x00FF, cntLeadZeros(0x00FF))
	fmt.Printf("0x%x leading ones = %v\n\n", 0x00FF, cntLeadOnes(0x00FF))
}
