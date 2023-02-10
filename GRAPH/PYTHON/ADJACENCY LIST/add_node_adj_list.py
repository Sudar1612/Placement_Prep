def add_node(ver):

    #check if the node is alreay there in graph or not
    if ver in graph:
        print(ver,"is already present!")
        return
    
    #if it is not present add it
    graph[ver]=[]

graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')

print(graph)