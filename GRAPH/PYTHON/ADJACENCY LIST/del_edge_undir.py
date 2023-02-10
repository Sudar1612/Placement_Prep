def add_node(ver):

    #check if the node is alreay there in graph or not
    if ver in graph:
        print(ver,"is already present!")
        return
    
    #if it is not present add it
    graph[ver]=[]

def add_edge_undir_unweigh(ver1,ver2):

    #check if both nodes are in graph or not
    if ver1 not in graph:
        add_node(ver1)
    if ver2 not in graph:
        add_node(ver2)
    
    #append both vertices

    graph[ver1].append(ver2)
    graph[ver2].append(ver1)

def add_edge_undir_weigh(ver1,ver2,cost):

    if(ver1 not in graph):
        add_node(ver1)
    if(ver2 not in graph):
        add_node(ver2)
    graph[ver1].append([ver2,cost])
    graph[ver2].append([ver1,cost])



#---------------------------------new code---------------------------------#

def del_edge_undir(ver1,ver2):

    #check if both nodes are in graph or not 
    if ver1 not in graph:
        print(ver1,"is not in graph")
    if ver2 not in graph:
        print(ver2,"is not in graph")
    else:
        #check if both vertices have connection
        #no need check if ver1 in ver2 since it is an undirected graph
        if ver2 in graph[ver1]:
             graph[ver1].remove(ver2)
             graph[ver2].remove(ver1)

#---------------------------------ends here---------------------------------#
graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')

add_edge_undir_unweigh('A','B')
add_edge_undir_unweigh('C','D')
add_edge_undir_unweigh('D','E')

add_edge_undir_weigh('A','B',12)
add_edge_undir_weigh('C','D',5)
add_edge_undir_weigh('B','E',2)

print(graph)

del_edge_undir('C','D')

print(graph)