package strings

// StringContains
// returns True if any string in s contains k
func StringContains(ss []string, k string) bool {

	for _, s := range ss {
		// check if s contains k
		for i := 0; i < len(s)-len(k); i++ {

			for j:=0; j < len(k); j++ {
				if s[i+j] != k[j] {
					break
				}

				if j == len(k)-1 {
					return true
				}
			}

		}
	}

	return false
}

