# Edit Distance Example in Python (Levenshtein Distance)
# A way to quantifying how dissimilar two strings are to one another


def edit_distance(s1, s2, len_s1, len_s2):

    if len_s1 == 0:
        return len_s2

    if len_s2 == 0:
        return len_s1

    cost = 0

    if s1[len_s1 - 1] != s2[len_s2 - 1]:
        cost = 1

    return min(edit_distance(s1, s2, len_s1 - 1, len_s2) + 1,
               edit_distance(s1, s2, len_s1, len_s2 - 1) + 1,
               edit_distance(s1, s2, len_s1 - 1, len_s2 - 1) + cost)

s1, s2 = 'Hello', 'Jello'
print(edit_distance(s1, s2, len(s1), len(s2)))
