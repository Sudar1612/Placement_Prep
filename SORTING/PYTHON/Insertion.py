def Insertion(num_list,leng):
    for out in range(leng):
        for inner in range(out):
            if(num_list[out]<num_list[inner]):
                num_list[out],num_list[inner]=num_list[inner],num_list[out]

num_list=[25,85,45,3,0]
Insertion(num_list,len(num_list))
print(num_list)