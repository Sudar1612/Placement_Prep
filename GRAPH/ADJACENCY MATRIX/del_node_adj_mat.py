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
         
#-----------------------------------------new code---------------------------------------------#

def del_node(ver):
   global node_count

   #check if the node is there in graph or not
   if ver not in nodes:
      print(ver,"is not present in graph")
      return
   
   #find the index of vertex
   ind=nodes.index(ver)

   #remove from nodes list and decrement the nodes count
   nodes.remove(ver)
   node_count-=1

   #remove the node from the graph
   graph.pop(ind)

   #remove the node every row
   for row in graph:
      row.pop(ind)

#------------------------------------------ends here---------------------------------------------#
nodes=[]
graph=[]
node_count=0
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')

print_graph()

del_node('D')

print_graph()