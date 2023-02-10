def add_node(ver):

    #check if the node is alreay there in graph or not
    if ver in graph:
        print(ver,"is already present!")
        return
    
    #if it is not present add it
    graph[ver]=[]

def add_edge_dir_weigh(ver1,ver2,cost):

    if(ver1 not in graph):
        add_node(ver1)
    if(ver2 not in graph):
        add_node(ver2)
    graph[ver1].append([ver2,cost])

def add_edge_undir_weigh(ver1,ver2,cost):

    if(ver1 not in graph):
        add_node(ver1)
    if(ver2 not in graph):
        add_node(ver2)
    graph[ver1].append([ver2,cost])
    graph[ver2].append([ver1,cost])

#------------------------------------------new code-------------------------------#

def del_node_weigh(ver):
     
     #check if the node is in graph or not
     if ver not in graph:
         print(ver,"is not in graph")
     else:
         graph.pop(ver)

         for val in graph.values():
             for inner in val:
                 if ver in inner:
                     val.remove(inner)
#-------------------------------------------ends here-------------------------------#

graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')

add_edge_dir_weigh('A','B',12)
add_edge_dir_weigh('C','D',5)
add_edge_dir_weigh('B','E',2)

add_edge_undir_weigh('C','B',12)
add_edge_undir_weigh('A','D',5)
add_edge_undir_weigh('D','E',2)

print(graph)

del_node_weigh('D')

print(graph)