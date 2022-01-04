def solution(x,y):
  diagonal_number = x+y-1
  diagonal_first_number = diagonal_number/2*(1+diagonal_number) # sum or arithmetic progression
  return str(int(diagonal_first_number-(y-1)))


print(solution(3,2))
print(solution(5,10))
