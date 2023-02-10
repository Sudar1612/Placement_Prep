def add_node(ver):

    #check if the node is alreay there in graph or not
    if ver in graph:
        print(ver,"is already present!")
        return
    
    #if it is not present add it
    graph[ver]=[]

#---------------------------------new code------------------------------#

def add_edge_undir_unweigh(ver1,ver2):

    #check if both nodes are in graph or not
    if ver1 not in graph:
        add_node(ver1)
    if ver2 not in graph:
        add_node(ver2)
    
    #append both vertices
    graph[ver1].append(ver2)
    graph[ver2].append(ver1)


#---------------------------------ends here---------------------------------#

graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')

add_edge_undir_unweigh('A','B')
add_edge_undir_unweigh('C','D')

print(graph)