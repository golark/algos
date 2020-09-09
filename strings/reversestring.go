package main

import log "github.com/sirupsen/logrus"

func reverseString(r []rune) {

	// return condition
	if len(r) <= 1 {
		return
	}

	// logic
	r[0], r[len(r)-1] = r[len(r)-1], r[0]

	// recursion
	reverseString(r[1:len(r)-1])
}

func main() {

	s := "Hello World!"
	r := []rune(s)

	reverseString(r)

	log.WithFields(log.Fields{"r:":string(r)}).Info("")
}
