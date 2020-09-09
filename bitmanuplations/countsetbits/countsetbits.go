package main

import (
	"fmt"
	"math/bits"
	"unsafe"
)

func cntSetBits(b uint) uint {

	var i uintptr
	var setCnt uint
	for i=0;i<unsafe.Sizeof(b);i++ {

		for k:=0;k<8;k++ {

			// count set bits
			setCnt += b & 0x1
			b = b >>1
		}
	}

	return setCnt

}


func main() {

	fmt.Printf("0xFF set bits :%v\n\n", cntSetBits(0xFF))


	// use bits library
	fmt.Printf("%v",bits.OnesCount(0xff))
}
