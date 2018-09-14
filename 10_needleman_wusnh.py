# Needleman-Wusnh Algorithm Example with Python

import sys


def needleman_wusnh(s1, s2, match, mismatch, gap):
    cols, rows = len(s1) + 1, len(s2) +1

    # create the matrix
    matrix = [[0 for i in range (cols)] for i in range(rows)]

    # getting the traceback to build the alignment
    traceback = {}

    # fill the first line
    matrix[0][0] = 0
    for i in range(1, cols):
       matrix [0][i] = matrix[0][i-1] + gap
       traceback[(0,i)] = (0, i - 1)
    for i in range(1, rows):
        matrix[i][0] = matrix[i - 1][0] + gap
        traceback[(i,0)] = (i - 1, 0)
    
    def max_value(i,j):
        left_diagonal = matrix[i - 1][j - 1] + (match if s2[i - 1] == s1[j - 1] else mismatch)
        top = matrix[i - 1][j] + gap
        left = matrix[i][j - 1] + gap

        max_v = max([left_diagonal, top, left])

        # verify the greater value
        if max_v == left_diagonal:
            traceback[(i,j)] = (i - 1, j - 1)
        elif max_v == top:
            traceback[(i,j)] = (i - 1, j)
        else:
            traceback[(i,j)] = (i, j - 1)
        
        return max_v

    # fill the rest of the matrix
    for i in range(1, rows):
        for j in range (1, cols):
            matrix[i][j] = max_value(i,j)
    
    s1_result, s2_result = '',''
    i,j = rows - 1, cols - 1

    while True:
        i_next, j_next = traceback[(i,j)]

        if (i - 1) == i_next and (j - 1) == (j - 1) == j_next: # left diagonal
            s1_result += s1[j_next]
            s2_result += s2[i_next]
        elif (i - 1) == i_next and j == j_next: # top
            s1_result += '-'
            s2_result += s2[i_next]
        elif i == i_next and (j - 1) == j_next: # left
            s1_result += s1[j_next]
            s2_result += '-'
        
        i, j = i_next, j_next

        if not i and not j:
            break   
    
    s1_result, s2_result = s1_result[::-1], s2_result[::-1]

    print('{0}\n{1}'.format(s1_result, s2_result))

if __name__ == "__main__":

    len_args = len(sys.argv)

    if len_args == 6:
        s1, s2 = sys.argv[1], sys.argv[2]
        match, mismatch, gap = sys.argv[3], sys.argv[4], sys.argv[5]

        needleman_wusnh(s1, s2, int(match), int(mismatch), int(gap))

    else:
        print('\nExecute:\n\tpython 10_needleman_wusnh.py <sequency1> <sequency2> <match> <mismatch> <gap>')
        print('\nExample:\n\tpython 10_needleman_wusnh.py GCATGCU GATTACA 1 -1 -1\n')
