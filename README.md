- Algorithms are method for solving problems and data structures are methods for storing information. Combination of the two might just solve your next challenge
- Implementations are in Go and Python

## Algorithms
    .
    ├── binary_search                                             # divide and counquer search
    |   ├── search_for_number.py                                  # search for the given number in BST
    |   ├── smallest_greater_letter.py                            # 
    |   ├── smallest_greater_number.py                            # smallest number in sequence greater than threshold
    ├── cyclic_sort                                               # sort numbers run from 1 to n 
    |   ├── cyclic_sort.py                                        # sort given numbers 1 to n  
    |   ├── find_all_missing_numbers.py                           # find all missing in sequence 1 to n  
    |   ├── find_duplicate_numbers.py                             # determine duplicates in sequence 1 to n
    |   ├── find_missing_number.py                                # find single mising number in sequence 1 to n
    ├── fast_slow_pointers                                        # hare & Tortoise algorithm
    |   ├── linked_list_cycle_check.py                            # determines if linked list has cyclic reference 
    ├── linkedlist                                                #
    |   ├── inplace_reversal.py                                   # reverse single linked list without using extra space
    |   ├── rotate_by_k.py                                        # rotate left or right by k
    ├── merge_intervals                                           #
    |   ├── merge_overlapping_intervals.py                        # given a set of intervals, merge if overlapping
    |   ├── intersection_of_intervals.py                          # 
    |   ├── free_interval.py                                      #
    ├── sequence_calculation                                      #
    |   ├── max_sum_non_adjacent_elements.py                      #   
    |   ├── nth_fibonacci.py                                      #  
    |   ├── monotonic_array.py                                    # sequence is all increasing or decreasing 
    |   ├── product_sum.py                                        # [x+y]=x+y [x,[y,z]]=x+2*(y+z)...
    ├── sliding_window                                            # two moving pointers
    |   ├── sum_of_subarray.py                                    # return running sum of each window of size K
    |   ├── max_sum_of_subarray.py                                # return max of sum of subarray K
    |   ├── smallest_subarray_of_sum_greater_than.py              #
    |   ├── longest_substring_with_K_distinct_characters.py       # 
    |   ├── longest_substring_with_no_repeating_characters.py     #
    ├── sorting                                                   #
    |   ├── selection_sort.py                                     # 
    |   ├── insertion_sort.py                                     # 
    |   ├── bubble_sort.py                                        # 
    |   ├── quick_sort.py                                         #
    ├── sequencecalculation                                       #
    |   ├── smallestdifference.go                                 # smallest difference between 2 unsorted arrays
    ├── stack                                                     #
    |   ├── palindromne.go                                        # check if given string is a palindrome
    ├── top_k_elements                                            # heap based algorithms
    |   ├── k_closest_numbers.py                                  # k closest numbers to given integer X
    |   ├── kth_maximum_number.py                                 # 
    |   ├── min_k_numbers.py                                      # 
    |   ├── top_k_frequent_numbers.py                             # 
    |   ├── top_k_numbers.py                                      # 
    ├── tree_breadth_first_search                                 # 
    |   ├── binary_tree_level_order_traversal.py                  # 
    |   ├── binary_tree_reverse_level_order_traversal.py          #  
    |   ├── binary_tree_zigzag_order_traversal.py                 # 
    |   ├── binary_tree_level_average.py                          # 
    |   ├── binary_tree_connect_level_order_siblings.py           # 
    |   ├── binary_tree_right_view.py                             # 
    ├── tree_depth_first_search                                   # 
    |   ├── all_paths_for_a_sum.py                                # return number of paths with given sum 
    |   ├── binary_tree_path_sym.py                               # check if there is a path with given sum
    |   ├── closest_value_in_bst.py                               # find closest value to target in BST
    |   ├── branch_sums.py                                        # return a list of branch sums of BST
    |   ├── branch_sums.go                                        # 
    |   ├── flip_sideways.py                                      # flip binary tree sideways
    ├── two_pointers                                              # 
    |   ├── pair_with_target_sum.py                               # given sorted array, find a pair with target sum
    |   ├── two_numbers_target_sum.py                             # similar to pair_with_target_sum but unsorted array
    |   ├── remove_duplicates.py                                  # remove duplicates in sorted array
    |   ├── triplet_sum_to_zero.py                                # unsorted array triplets sum to zero
    |   ├── dutch_national_flag.py                                # sort array in place consisting of elements 0,1,2
    |   ├── strings_with_backspaces.py                            # given strings with backspace characters check if they are equal
    |   ├── minimum_window_sort.py                                # length of the smallest subarray, when sorted will sort the whole array
    |   ├── maximum_profit.py                                     # 
    ├── LICENSE                                                   # Apache 2.0
    ├── README.md                                                 # 
    └ 
    
### Copyright and license

Code and documentation released under the [Apache 2.0 License](LICENSE) 
 
## algorithm strategy
- brute force: considering all the possibilities without a regard for performance or space improvements
- greedy: choose most obvious, immediate benefit at each stage of the algorithm
- recursion: dissecting a problem into smaller instances of the same problem
- divide-and-conquer: divide the problem into atomic units,

## complexity/space evaluation
- Best, Worst, Average Case analysis
- Asymptotic analysis is time/space complexity assessment for very large input data set. One example is Big O

### Big O
- drop multiplicative constants, drop all but highest order polynomial, for example complexity 5n^2+2n+3 ~= O(n^2)
- Two algorithms with  O(n) will be withing a constant factor from each other, for practical purposes they are considered equally good
- Big O is preferred to Big Theta or other evaluation metrics due to better worst-case analysis

### abstract data type (ADT)
- defined by behaviour rather than its representation
- queue, list, stack where we have a set of defined semantics ( behaviours ) but the internal representation is decouple from the user
- heaps are data structures that are based on priority queues which is an abstract data type that has 3 defined behaviours: 
 is_empty, add_element and pop_element 

## stack
- is a abstract data type
- ordered as last-in-first-out (LIFO)
- main operations: push, pop, peek, isempty
- use case: Reversing a String/List, Detecting Palindromes
- implementation: 
1. arrays: need to grow array when size is full or shrink the array, can double when full ( similar to golang slices ), 
faster insertion time  when not changing the capacity, consumes less space 
2. linked-list: more space, constant insertion/removal time ( assuming pushin/popping from head ), consumes more space
- stacks are LIFO, queues are FIFO

## linked list
- start of a linked list is referred to as "head"
- each node contains Data and references to the next/previous nodes
- the last node is null ( linked list termination ), in Python (None)
              Node
         ------ ------           ------ ------
head -> |      |      | ------> |      |      |
        | Data | next |         | Data | next |
        |      |      |         |      |      |
         ------ ------           ------ ------

### array vs linked list

  |                | array | linked list |
  | -----          | ----- | ------      |         
  | access element | O(1)  | O(n)        | 
  | insert/delete  | O(n)  | O(1)        |
- accessing the n'th element of a linked list is O(n), whereas for array  O(1)
- insertion into linked list is O(1) since only manuplation of a couple of pointers
- arrays are contagious memory which provides more predictable access time, linked list access time is less predictable

## Binary Tree
- tree data structure where each node has 2 children nodes
- depth of a node:  the length of path from node to root
- height of a tree: the length of path from node to deepest node
- complete binary tree: every level except the last is filled, and the last level is filled by left-most
- full binary tree: each node has either 2 children or none
- The BST ( Binary Search Tree ) property states that every node on the right subtree has to be larger than the current node, and every node on the left subtree has to be smaller than the current node.

