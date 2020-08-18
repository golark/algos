

# ceasar_cypher_encryptor
# rotate each letter by k
# wrap around alphabet
def ceasar_cypher_encryptor(s, k):

    ciphered = []
    overflow_adjust = ord('z') - ord('a')
    for c in s:
        new_c = ord(c) + k
        if new_c > ord('z'): # overflow adjustment
            new_c = new_c - overflow_adjust
        ciphered.append(chr(new_c))

    return "".join(ciphered)


def main():
    res = ceasar_cypher_encryptor("abcdefgxyz", 2)
    print(f'{res}')


if __name__ == "__main__":
    main()