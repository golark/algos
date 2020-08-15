algorithms - method for solving problems
data structures - methods for storing information
"Good programmers think about data structures and their relationships between them rater than code" Linus Tovalds
##### Directory structure and files
    .
    ├── sliding_window                                            # two moving pointers
    |   ├── sum_of_subarray.py                                    # return running sum of each window of size K
    |   ├── max_sum_of_subarray.py                                # return max of sum of subarray K
    |   ├── smallest_subarray_of_sum_greater_than.py              # 
    |   ├── longest_substring_with_K_distinct_characters.py       # 
    |   ├── longest_substring_with_no_repeating_characters.py     # @todo
    ├── merge_intervals                                           #
    |   ├── merge_overlapping_intervals.py                        # given a set of intervals, merge if overlapping
    |   ├── intersection_of_intervals.py                          # 
    |   ├── free_interval.py                                      # @todo https://www.educative.io/courses/grokking-the-coding-interview/YQykDmBnvB0
    ├── linked_list                                               #
    |   ├── inplace_reversal.py                                   # 
    |   ├── rotate_by_k.py                                        #
    ├── fast_slow_pointers                                        # hare & Tortoise algorithm
    |   ├── linked_list_cycle_check.py                            #
    ├── top_k_elements                                            # heap based algorithms
    |   ├── top_k_elements.py                                     #
    ├── two_pointers                                              # 
    |   ├── pair_with_target_sum.py                               # given sorted array, find a pair with target sum
    |   ├── remove_duplicates.py                                  # remove duplicates in sorted array
    |   ├── triplet_sum_to_zero.py                                # @todo: unsorted array triplets sum to zero
    |   ├── dutch_national_flag.py                                # @todo: sort array in place of elements 0,1,2
    |   ├── strings_with_backspaces.py                            # given strings with backspace characters check if they are equal
    |   ├── minimum_window_sort.py                                # @todo: length of the smallest subarray, when sorted will sort the whole array
    ├── tree_breadth_first_search                                 # 
    |   ├── binary_tree_level_order_traversal.py                  # 
    ├── LICENSE                                                   # Apache 2.0
    ├── README.md                                                 # 
    └ 
    
### Copyright and license

Code and documentation released under the [Apache 2.0 License](LICENSE) 
 


# solution approaches
- brute force: considering all the possibilities without a regard for performance or space improvements
- greedy: choose most obvious, immediate benefit at each stage of the algorithm
- recursion: dissecting a problem into smaller instances of the same problem
- divide-and-conquer: divide the problem into atomic units,

1. sliding_window
- two moving pointers
- combined with hash maps to find occurrence of characters, permutation of elements

2. fast & slow pointers
- find middle of linked list
- find cyclic linkedlist nodes, lenght of the cyclic section
3. Sliding Window
- smallest subarray with sum larger than k
- string containing anagram of pattern ( dictionary with sliding window)
4. XOR
- missing number in sequence
- find missing duplicate number ( XOR all numbers )

# evaluation
- Best, Worst, Average Case analysisi
- time/space complexity
- Asymptotic analysis is time/space complexity asssessment for very large input data set. One example is Big O

## Big O
- drop multiplicative contants, drop all but highest order polynomial, for example complexity 5n^2+2n+3 ~= O(n^2)
- Two algithtms with  O(n) will be withing a constant factor from each other, for practical purposes they are considered equally good
- Big O is preffered to Big Theta or other evaliation metrics due to better worst-case analysis

#### General Guidelines
- Whenever a list or array gets iterated over an integer multiple times .
- When you see a problem where the number of elements in the problem space gets halved each time, that will most probably be in O(log n)O(logn) runtime.
- Whenever you have a singly nested loop, the problem is most likely in quadratic time.

# abstract data type (ADT)
- defined by behaviour rather than its representation
- queue, list, stack where we have a set of defined semantics ( behaviours ) but the iternal representation is decouple from the user

# stack
- abstract data type
- ordered as last-in-first-out (LIFO)
- main operations: push, pop, peek, isempty
- use case: Reversing a String/List, Detecting Palindromes
- implementation: 
1. arrays: need to grow array when size is full or shrink the array, can double when full ( similar to golang slices ), 
faster insertion time  when not changing the capacity, consumes less space 
2. linked-list: more space, constant insertion/removal time ( assuming pushin/popping from head ), consumes more space

## stack vs queue
- stacks are LIFO, queues are FIFO

# linked list
- start of a linked list is reffered to as "head"
- each node contains Data and references to the next/previous nodes
- the last node is null ( linked list termination ), in Python (None)
              Node
         ------ ------           ------ ------
head -> |      |      | ------> |      |      |
        | Data | next |         | Data | next |
        |      |      |         |      |      |
         ------ ------           ------ ------

@todo: merge 2 sorted linked lists
@todo: sort linked list
@todo: remove duplicates
@todo: N'th to last node
@todo: count occurances recursive
@todo: isPalindrome

## array vs linked list

  |                | array | linked list |
  | -----          | ----- | ------      |         
  | access element | O(1)  | O(n)        | 
  | insert/delete  | O(n)  | O(1)        |

- accessing the n'th element of a linked list is O(n), whereas for array  O(1)
- insertion into linked list is O(1) since only manuplation of a couple of pointers
- arrays are contagious memory which provides more predictable access time, linked list access time is less predictable

### single linked list
- tail is null/None
- pointer/reference in one direction

### double linked list
- pointer/reference in both directions

### circular
- tail points to the Head instead of null/None

# Binary Tree
- tree data structure where each node has 2 children nodes
- depth of a node:  the length of path from node to root
- height of a tree: the length of path from node to deepest node
- complete binary tree: every level except the last is filled, and the last level is filled by left-most
- full binary tree: each node has either 2 children or none
- The BST ( Binary Search Tree ) property states that every node on the right subtree has to be larger than the current node, and every node on the left subtree has to be smaller than the current node.

@todo: calculate size of a binary tree

## tree traversal
- depth first or breath first

# sorting
- callbacks are used for making sorting algorithm generic
- in Java, "comparable" interfaces are used which has compareTo method
- in C, function pointers are used
- in python lambda functions, or formal functions are first class citizens that can be used as a callback


## selection sort
- find min or max, place and iterate O(n^2)

## insertion sort

## shell sort

## shuffling
- breaks the sorted list almost like dech shuffling

### knuth shuffle


### bubblesort
- compare adjacent elements, swap if necessaary, iterate O(n^2)

### mergesort
@todo

### quicksort
@todo

@todo pascals algorithm
@todo eucledian algorithm for greatest common divisor
@todo: buy and sell stock