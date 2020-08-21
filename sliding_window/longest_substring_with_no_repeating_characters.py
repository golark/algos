

def longest_substring_with_k_distinct_characters(str, K):

    s = set()
    p = 0
    longest = 0
    for q in range(len(str)):

        s.add(str[q])

        # check size of set
        if len(s) <= K:
            longest = max(longest, q-p+1)
        else:
            while len(s) > K:

                if str[p] in s:
                    s.remove(str[p])
                p = p +1
                s.add(str[p])

    return longest


def main():
    res = longest_substring_with_k_distinct_characters("aabccadwgedagr", 2)

    print(f'{res}')


if __name__ == "__main__":
    main()