def add_node(ver):

    #check if the node is alreay there in graph or not
    if ver in graph:
        print(ver,"is already present!")
        return
    
    #if it is not present add it
    graph[ver]=[]

#----------------------------------------new code------------------------------------#

def add_edge_dir_unweigh(ver1,ver2):

    if(ver1 not in graph):
        add_node(ver1)
    if(ver2 not in graph):
        add_node(ver2)
    graph[ver1].append(ver2)

#-----------------------------------------ends here-----------------------------------#

graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')

add_edge_dir_unweigh('A','B')
add_edge_dir_unweigh('B','C')
add_edge_dir_unweigh('D','E')

print(graph)