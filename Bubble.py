def ascending(num_list,ran):
    while(ran):
        for ind in range(len(num_list)-1):
            if(num_list[ind]>num_list[ind+1]):
                num_list[ind+1],num_list[ind]=num_list[ind],num_list[ind+1]
        ran-=1
    print(num_list)

def desending(num_list,ran):
    while(ran):
        for ind in range(len(num_list)-1):
            if(num_list[ind]<num_list[ind+1]):
                num_list[ind+1],num_list[ind]=num_list[ind],num_list[ind+1]
        ran-=1
    print(num_list)

num_list=[10,15,4,23,0]
ran=len(num_list)-1
ascending(num_list,ran)
desending(num_list,ran)