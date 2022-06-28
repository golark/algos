package main

import (
    "fmt"
    "strconv"
)

func reverseSlice(s []interface{}) {
    for i, k := 0, len(s)-1; i < k; i, k = i+1, k-1{
        s[i], s[k] = s[k], s[i]
    }
}

func reverseSliceRecursive(s []interface{}) {
   if len(s) <=1 {
       return
   }

   s[0], s[len(s)-1] = s[len(s)-1], s[0]

   reverseSliceRecursive(s[1:len(s)-1])
}

func main() {
    s := make([]interface{}, 100)

    for i := range s {
        if i%2 == 0 {
            s[i] = strconv.Itoa(i) + "a"
        } else {
            s[i] = float32(i)
        }

    }
    reverseSlice(s)
    reverseSliceRecursive(s)
    fmt.Printf("slice = %v", s)
}
