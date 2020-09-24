package main

import (
	"errors"
	log "github.com/sirupsen/logrus"
)

// fifo
// contains only integers
// new items are appended to the bottom and removed from the bottom
type fifo struct{
	queue []int
}

// NewFifo
// factory function
func NewFifo() *fifo {
	f := fifo{ make([]int, 0)}
	return &f
}

// Enque
// append to the bottom of the queue
func (f *fifo) Enque(i int) {
	f.queue = append(f.queue, i)
}

// Deque
// pop from the bottom of the queue
func (f *fifo) Deque() ( int, error) {

	if len(f.queue) == 0 {
		return 0, errors.New("trying to deque from empty queue")
	}

	// get the value from the bottom of the queue
	i := f.queue[len(f.queue)-1]

	// pop from the queue
	f.queue = f.queue[:len(f.queue)-1]

	return i, nil
}


func main() {
	f := NewFifo()

	for i:=0;i<10;i++ {
		f.Enque(i)
	}

	for i:=0;i<10;i++ {
		i, err := f.Deque()
		if err != nil {
			log.WithFields(log.Fields{"err":err}).Error("")
			break
		}
		log.WithFields(log.Fields{"i":i}).Info("popped")

	}

}
