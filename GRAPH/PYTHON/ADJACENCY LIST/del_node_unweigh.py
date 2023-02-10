def add_node(ver):

    #check if the node is alreay there in graph or not
    if ver in graph:
        print(ver,"is already present!")
        return
    
    #if it is not present add it
    graph[ver]=[]

def add_edge_dir_unweigh(ver1,ver2):

    if(ver1 not in graph):
        add_node(ver1)
    if(ver2 not in graph):
        add_node(ver2)
    graph[ver1].append(ver2)

def add_edge_undir_unweigh(ver1,ver2):

    #check if both nodes are in graph or not
    if ver1 not in graph:
        add_node(ver1)
    if ver2 not in graph:
        add_node(ver2)
    
    #append both vertices
    graph[ver1].append(ver2)
    graph[ver2].append(ver1)

#----------------------------------------------------new code----------------------------------------#

def del_node_unweigh(ver):
    
    #check if the node is present in graph or not
    if ver not in graph:
        print(ver,"not in graph")
    else:
        graph.pop(ver)
        for val in graph.values():
            if ver in val:
                val.remove(ver)

#-----------------------------------------------------ends here---------------------------------------#

graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')

add_edge_dir_unweigh('A','B')
add_edge_dir_unweigh('B','C')
add_edge_dir_unweigh('D','E')
add_edge_undir_unweigh('A','E')
add_edge_undir_unweigh('C','D')

print(graph)

#function call
del_node_unweigh('B')

print(graph)