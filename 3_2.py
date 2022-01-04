def solution(n):
    n = int(n)
    operations = 0
    while n > 1:
        # if it is even
        if n % 2 == 0:         
            n = n // 2
        # if not even, check if the number bellow or above it is divisible
        # by 4 - that means we can divide it twice
        # it can be shown that this is optimal route
        elif n == 3 or n % 4 == 1: 
            n = n - 1
        else:                     
            n = n + 1
        operations += 1
    return operations


print(solution("0"))

def BFS_SP(n):
    n = int(n)
    explored = []
	
	# Queue for traversing the
	# graph in the BFS
    queue = [[n]]
	
	# If the desired node is
	# reached
    if n == 1:
        return 0
	
	# Loop to traverse the graph
	# with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
		
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = get_neighbours(node)

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
        
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == 1:
                    return len(new_path) - 1
            
            explored.append(node)
      
    return 


def get_neighbours(n):
    neighbours = []
    # division if even
    if n % 2 == 0:
        neighbours.append(n//2)
    else:
        neighbours.extend([n-1, n+1])

    #print(neighbours)
    return neighbours


print(BFS_SP(1))