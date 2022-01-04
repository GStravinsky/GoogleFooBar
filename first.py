

def solution(x, y):
  set_add_id = set.symmetric_difference(set(x),set(y))
  
  return set_add_id.pop()


a = [1,2,3,4,5,6]
b=[1,2,9,3,4,5,6]

print(solution(a,b))


