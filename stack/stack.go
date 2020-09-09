package stack

import (
	"errors"
	"fmt"
)

type stckSlice struct {
	inner []int
}

func New() *stckSlice {
	s := stckSlice{}
	return &s
}

func (s *stckSlice) Push(i int) {
	s.inner = append(s.inner, i)
}

func (s *stckSlice) Pop() (int, error) {

	// pop single element from the top
	if s.IsEmpty() {
		return 0, errors.New("empty Stack, cant pop")
	}
	i := s.inner[len(s.inner)-1]

	// remove item from inner slice
	s.inner	= s.inner[0:len(s.inner)-1]

	return i, nil
}

func (s *stckSlice) IsEmpty() bool {
	return len(s.inner) == 0
}

func (s *stckSlice) Peek() (int, error) {

	if s.IsEmpty() {
		return 0, errors.New("Empty Stack")
	}

	return s.inner[len(s.inner)-1], nil
}

func (s *stckSlice) ViewStack() {
	fmt.Printf("%v", s.inner)
}