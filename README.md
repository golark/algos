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
- Best, Worst, Average Case analysis
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
- distinguishing characteristic of a stack is that insertion and removal takes place at the same end
- ordered as last-in-first-out 
- main operations:push, pop, peek, isempty
- Reversing a String/List, Detecting Palindromes
@todo: generic stack #golang
@todo: rune conversions in golang
@todo: stringer interface support

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

### selection sort
- find min or max, place and iterate O(n^2)

### bubblesort
- compare adjacent elements, swap if necessaary, iterate O(n^2)

### mergesort
@todo

### quicksort
@todo

@todo pascals algorithm
@todo eucledian algorithm for greatest common divisor
@todo: buy and sell stock