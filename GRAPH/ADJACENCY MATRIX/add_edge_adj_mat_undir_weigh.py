def add_node(newNode):
   global node_count

   #check if the new node is already is present in node
   if newNode in nodes:
      print(newNode,"Oops! Already Present in Graph")
      return
   
   #if not add in nodes and increase node count
   node_count+=1
   nodes.append(newNode)

   #add one column in each row
   for row in graph:
      row.append(0)
    
   #add one row in matrix
   temp=[]
   for row in range(node_count):
      temp.append(0)
   graph.append(temp)

def print_graph():
   for row in range(node_count):
      for col in range(node_count):
         print(graph[row][col],end=' ')
      print()
         

#---------------------------------------new code-----------------------------------------#

def add_edge_undir_weigh(ver1,ver2,cost):
   if ver1 not in nodes:
      add_node(ver1)
   if ver2 not in nodes:
      add_node(ver2)
   
   ind1=nodes.index(ver1)
   ind2=nodes.index(ver2)
   graph[ind1][ind2]=cost
   graph[ind2][ind1]=cost

#---------------------------------------ends here-------------------------------------------------#
nodes=[]
graph=[]
node_count=0
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')

add_edge_undir_weigh('A','B',9)
add_edge_undir_weigh('C','D',6)

# print(graph)+
print_graph()