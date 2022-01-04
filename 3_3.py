""" 
The solution relies on: https://en.wikipedia.org/wiki/Absorbing_Markov_chain#Absorbing_probabilities
1. Split the input:
    a) remove the rows that only contain zero - memorize the row index removed
    b) R: get the cells that are out of the zero row a) region but only contains column that corresponds to the indices of the rows removed due to zeros
    c) Q: the remainder of matrix is Q

2. Get N:
    a) implement matrix inverse
    b) implement "deduce from identity" method 
    c) N: invert deduced Q from identity matrix

3. Get B:
    a) implement matrix multiplication
    b) multiply N*R

4. Get the result:
    a) (1,0)*B
    b) extract the common deminator with Fraction(a,b).denominator and numerator

Caveats:
Dealing with fractions: https://docs.python.org/2.7/library/fractions.html
"""