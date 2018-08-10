# Hamming Distance example in Python
# Compare two strings and find the positions where the symbols are different
# Example: hamming(0101, 0100) = 1 cause only in the 4th position the symbols are different
# Example: hamming(0101, 1110) = 3 cause in the 1st, 3th and 4th positions the symbols are different


def hamming(v1, v2):

    s1, s2 = str(v1), str(v2) # turn the variables in strings values

    len_s1, len_s2 = len(s1), len(s2)
    if len_s1 != len_s2:
        raise ValueError('Different size between the variables')

    return sum(1 for i in range(len_s1) if s1[i] != s2[i])

#Running the examples
print(hamming('0101', '0100'))
print(hamming('0101', '1110'))

#Running an error example
print(hamming('0101', '11100'))