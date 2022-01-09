from fractions import Fraction, gcd

def solution(m):

    mat = Matrix(m)

    if (mat.matrix[0].count(0) == len(mat.matrix[0])) \
    or (mat.matrix[0].count(0) == len(mat.matrix[0])-1 and mat.matrix[0][0] != 0):
        result = [1]
        result.extend([0] * (len(mat.matrix)-1) )
        result.append(1)
        return result


    R,Q = split_the_matrix(mat)
    
    N = Q.deduce_from_identity().inverse() 
    B = N.multiply(R)

    result = parse_solution(B)
    return result

def parse_solution(b):
    probs_row = b.matrix[0]

    # getting lowest common multiplier of the denominators using greates common divisor
    # lcm(x,y)=x*y/gcd(x,y)
    lcm = reduce(lambda x,y: x*y.denominator/gcd(x,y.denominator), probs_row, 1)
    result = [(i*lcm).numerator for i in probs_row]
    result.append(lcm)

    return result

def split_the_matrix(m):

    terminal_states_indices = [ind for ind, row in enumerate(m.matrix) if check_if_terminal(row, ind)]
    transient_states = [row for ind, row in enumerate(m.matrix) if not check_if_terminal(row, ind)]
    transient_states_probabilities = [convert_to_probabilities(row) for row in transient_states]

    R_matrix, Q_matrix = make_R_Q_matrices(transient_states_probabilities, terminal_states_indices)


    return R_matrix, Q_matrix

def make_R_Q_matrices(matrix, terminal_indices):
    R_matrix = []
    Q_matrix = []
    for row in matrix:
        R_matrix.append([cell for idx, cell in enumerate(row) if idx in terminal_indices])
        Q_matrix.append([cell for idx, cell in enumerate(row) if idx not in terminal_indices])
    return Matrix(R_matrix), Matrix(Q_matrix)

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


class Matrix:
    def __init__(self, m):
        self.matrix = m 
    
    #### Matrix inversion using Gaussian method 

    def inverse(self):
        tmp = [[] for _ in self.matrix]
        for i,row in enumerate(self.matrix):
            assert len(row) == len(self.matrix)
            tmp[i].extend(row + [0]*i + [1] + [0]*(len(self.matrix)-i-1))
        self.__gauss(tmp)
        result = []
        for i in range(len(tmp)):
            result.append(tmp[i][len(tmp[i])//2:])
        return Matrix(result)
    
    def __eliminate(self, r1, r2, col, target=0):
        fac = (r2[col]-target) / r1[col]
        for i in range(len(r2)):
            r2[i] -= fac * r1[i]

    def __gauss(self, m):
        for i in range(len(m)):
            if m[i][i] == 0:
                for j in range(i+1, len(m)):
                    if m[i][j] != 0:
                        m[i], m[j] = m[j], m[i]
                        break
            for j in range(i+1, len(m)):
                self.__eliminate(m[i], m[j], i)
        for i in range(len(m)-1, -1, -1):
            for j in range(i-1, -1, -1):
                self.__eliminate(m[i], m[j], i)
        for i in range(len(m)):
            self.__eliminate(m[i], m[i], i, target=1)
        return m

    #### matrix multiplication  #####
    def __get_multiplied_matrix_cell(self, other, r, c):
        other_column = [row[c] for row in other]
        product = [self.matrix[r][i]*other_column[i] for i in range(len(other_column))]
        return sum(product)
        
    def multiply(self, other):  
        result_columns = len(other.matrix[0])
        result_rows = len(self.matrix)  
        result = [[0 for p in range(result_columns)] for q in range(result_rows)]
        for i in range(result_rows):
            for j in range(result_columns):
                result[i][j] = self.__get_multiplied_matrix_cell(other.matrix, i, j)
        return Matrix(result)


    def deduce_from_identity(self):
        result = [[0 for p in range(len(self.matrix))] for q in range(len(self.matrix[0]))]
        for row_idx, row in enumerate(self.matrix):
            for cell_idx, cell in enumerate(row):
                if row_idx == cell_idx:
                    result[row_idx][cell_idx] = 1-cell 
                else:
                    result[row_idx][cell_idx] = -cell 
        return Matrix(result)

    def __repr__(self):
        return str(self.matrix)


#### A bunch of testing stuff

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
testC = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]


assert(solution(testC)== [0, 3, 2, 9, 14])

assert(solution(
    [
        [0],
    ]
)) == [1, 1]

assert(solution(
    [
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
)) == [7, 6, 8, 21]

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
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

print(solution(testC))


