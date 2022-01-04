input = [[0,1,1,0], [0,0,0,1], [1,1,1,1], [1,1,0,0]]

input2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0]]

input3 = [[0,0,1,1], [1,1,1,1], [1,0,1,1], [0,0,1,1], [0,1,1,1], [0,0,0,0]]
import pprint
from collections import defaultdict

def solution(map):
    num_rows = len(map)
    num_columns = len(map[0])
    min_distance = num_rows + num_columns - 1

    adj_list = make_adj_list(map)
    distance = BFS_SP(adj_list, (0,0), (num_rows-1, num_columns-1))

    if distance == min_distance:
        return distance

    #if the default path was not shortest, let's remove walls
    distances = []
    for idx, row in enumerate(map):
        # find all walls in the row
        ones = [ i for i,j in enumerate(row) if j == 1]
        for one in ones:
            # remove wall
            map[idx][one] = 0

            adj_list_removed_wall = make_adj_list(map)
            distance_removed_wall = BFS_SP(adj_list_removed_wall, (0,0), (num_rows-1, num_columns-1))
            if distance_removed_wall is not None:
                distances.append(distance_removed_wall)

            if distance_removed_wall == min_distance:
                return distance_removed_wall
            # returning the wall back to the original map
            map[idx][one] = 1

    return min(distances)
  
  
from collections import defaultdict

def make_adj_list(input):
  adj_list = defaultdict()
  nodes = []

  # make a list of nodes
  for idx, row in enumerate(input):
    zeros = [(idx, i) for i,j in enumerate(row) if j == 0]
    nodes.extend(zeros)

  # check for the adjecent nodes for each node
  for node in nodes:
    possible = [(node[0], node[1]-1), (node[0]-1, node[1]), (node[0], node[1]+1), (node[0]+1, node[1])]
    adj_list[node] = [i for i in possible if i in nodes]
    
  return adj_list
  
  
def BFS_SP(graph, start, goal):
  explored = []
	
	# Queue for traversing the
	# graph in the BFS
  queue = [[start]]
	
	# If the desired node is
	# reached
  if start == goal:
    return
	
	# Loop to traverse the graph
	# with the help of the queue
  while queue:
    path = queue.pop(0)
    node = path[-1]
		
      # Condition to check if the
      # current node is not visited
    if node not in explored:
      neighbours = graph[node]

      # Loop to iterate over the
      # neighbours of the node
      for neighbour in neighbours:
        new_path = list(path)
        new_path.append(neighbour)
        queue.append(new_path)
        
        # Condition to check if the
        # neighbour node is the goal
        if neighbour == goal:
          return len(new_path)
      explored.append(node)
      
  return 
            
            


# a case when it does not always lead to the minimum distance
print(solution(input3))