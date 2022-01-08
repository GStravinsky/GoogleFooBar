from fractions import Fraction, gcd

def solution(m):

    if (m[0].count(0) == len(m[0])) or (m[0].count(0) == len(m[0])-1 and m[0][0] != 0):
        result = [1]
        result.extend([0] * (len(m)-1) )
        result.append(1)
        return result

    R,Q = split_the_matrix(m)
    
    N = inverse(deduce_m_from_identity(Q))
    B = multiply_matrices(N,R)

    result = parse_solution(B)
    return result

def parse_solution(b):
    to_fraction = b[0]
    # getting lowest common multiplier of the denominators using greates common divisor
    # lcm(x,y)=x*y/gcd(x,y)
    lcm = reduce(lambda x,y: x*y.denominator/gcd(x,y.denominator), to_fraction, 1)
    to_fraction = [(i*lcm).numerator for i in to_fraction]
    to_fraction.append(lcm)

    return to_fraction

def split_the_matrix(m):

    terminal_states_indices = [ind for ind, row in enumerate(m) if check_if_terminal(row, ind)]
    transient_states = [row for ind, row in enumerate(m) if not check_if_terminal(row, ind)]
    transient_states_probabilities = [convert_to_probabilities(row) for row in transient_states]

    R_matrix, Q_matrix = make_R_Q_matrices(transient_states_probabilities, terminal_states_indices)


    return R_matrix, Q_matrix

def deduce_m_from_identity(m):
    result = [[0 for p in range(len(m))] for q in range(len(m[0]))]
    for row_idx, row in enumerate(m):
        for cell_idx, cell in enumerate(row):
            if row_idx == cell_idx:
                result[row_idx][cell_idx] = 1-cell 
            else:
                result[row_idx][cell_idx] = -cell 
    return result

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
            prob_row.append(Fraction(oc,total_occurences))
    return prob_row
    
def check_if_terminal(row, idx):
    if (row.count(0) == len(row)) or (row.count(0) == (len(row)-1) and row[idx] != 0): 
        return True
    else:
        return False


#### Matrix inversion using Gaussian method 
def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret
 
#### matrix multiplication  #####
def getCell(m, n, r, c):
    n_column = [row[c] for row in n]
    product = [m[r][i]*n_column[i] for i in range(len(n_column))]
    return sum(product)
     
def multiply_matrices(m,n):  
    result_columns = len(n[0])
    result_rows = len(m)  
    result = [[0 for p in range(result_columns)] for q in range(result_rows)]
    for i in range(result_rows):
        for j in range(result_columns):
            result[i][j] = getCell(m, n, i, j)
    return result




testB = [[0, 275093, 17549739, 0, 0],
        [0, 0, 0, 25908539, 200000],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]]


testEmpty = [
    [0,0,0],
    [4,4,5],
    [4,7,8]
]
#print(solution(testEmpty))
testC = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]


# assert(solution(testC)== [0, 3, 2, 9, 14])

# assert(solution(
#     [
#         [0],
#     ]
# )) == [1, 1]

# assert(solution(
#     [
#         [0, 2, 1, 0, 0],
#         [0, 0, 0, 3, 4],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0],
#     ]
# )) == [7, 6, 8, 21]

testD = [[0, 1508, 3013, 0, 0],
        [0, 0, 0, 251, 208],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]]


testB = [[0, 275093, 17549739, 0, 0],
        [0, 0, 0, 25908539, 20],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]]

testEq = [
    [0,1,1,1],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
print(solution(testD))

