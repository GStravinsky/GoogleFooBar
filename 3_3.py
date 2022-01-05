""" 
The solution relies on: https://en.wikipedia.org/wiki/Absorbing_Markov_chain#Absorbing_probabilities
1. Split the input:
    a) remove the rows that only contain zero - memorize the row index removed
    b) convert the rest of the rows into probabilities - in the context of a row
    b) R: get the cells that are out of the zero row a) region but only contains column that corresponds to the indices of the rows removed due to zeros
    c) Q: the remainder of matrix is Q
    DONE

2. Get N:
    a) implement matrix inverse
    b) implement "deduce from identity" method 
    c) N: invert deduced Q from identity matrix
    DONE 
    
3. Get B:
    a) implement matrix multiplication
    b) multiply N*R

4. Get the result:
    a) (1,0)*B
    b) extract the common deminator with Fraction(a,b).denominator and numerator

Caveats:
Dealing with fractions: https://docs.python.org/2.7/library/fractions.html
"""

import fractions

def solution(m):
    R,Q = split_the_matrix(m)

    N = getMatrixInverse(deduce_m_from_identity(Q))
    return N

def split_the_matrix(m):

    terminal_states_indices = [ind for ind, row in enumerate(m) if check_if_terminal(row)]
    transient_states = [row for row in m if not check_if_terminal(row)]
    transient_states_probabilities = [convert_to_probabilities(row) for row in transient_states]

    R_matrix, Q_matrix = make_R_Q_matrices(transient_states_probabilities, terminal_states_indices)


    return R_matrix, Q_matrix

def deduce_m_from_identity(m):
    for row_idx, row in enumerate(m):
        for cell_idx, cell in enumerate(row):
           m[row_idx][cell_idx] = -cell 
    return m

def make_R_Q_matrices(matrix, terminal_indices):
    R_matrix = []
    Q_matrix = []
    for row in matrix:
        R_matrix.append([cell for idx, cell in enumerate(row) if idx in terminal_indices])
        Q_matrix.append([cell for idx, cell in enumerate(row) if idx not in terminal_indices])
    return R_matrix, Q_matrix

def convert_to_probabilities(row):
    total_occurences = sum(row)
    prob_row = []
    for oc in row:
        if oc == 0:
            prob_row.append(oc)
        else:
            prob_row.append(fractions.Fraction(oc,total_occurences))
    return prob_row

def check_if_terminal(row):
    if row.count(0) == len(row):
        return True
    else:
        return False

def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

testM = [
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]

print(solution(testM))