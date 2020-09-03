package twopointers

// IsPalindrome
// returns True if given string is a palindrome
// uses a two pointers which start from both ends of the string
// comparing and moving towards the middle of the string
// O(n) time, O(1) space
func IsPalindrome(s string) bool {

	p := 0
	q := len(s)-1
	for ;p < q ; {

		if s[p] != s[q] {
			return false
		}
		p += 1
		q -= 1
	}
	return true

}

