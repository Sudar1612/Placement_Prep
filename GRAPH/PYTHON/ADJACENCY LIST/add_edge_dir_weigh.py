def add_node(ver):

    #check if the node is alreay there in graph or not
    if ver in graph:
        print(ver,"is already present!")
        return
    
    #if it is not present add it
    graph[ver]=[]

#----------------------------------------new code------------------------------------#

def add_edge_dir_weigh(ver1,ver2,cost):

    if(ver1 not in graph):
        add_node(ver1)
    if(ver2 not in graph):
        add_node(ver2)
    graph[ver1].append([ver2,cost])

#-----------------------------------------ends here-----------------------------------#

graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')

add_edge_dir_weigh('A','B',12)
add_edge_dir_weigh('C','D',5)
add_edge_dir_weigh('B','E',2)
print(graph)