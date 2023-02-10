def findMini(num_list,leng,start):
    mini=99999
    for ind in range(start,leng,1):
        if(num_list[ind]<mini):
            mini=num_list[ind]
    return num_list.index(mini)

def Selection(num_list,leng):
    ran=1
    while(ran<=leng):
        ind=findMini(num_list,leng,ran-1)
        num_list[ran-1],num_list[ind]=num_list[ind],num_list[ran-1]
        ran+=1


num_list=[5,15,3,12,17,0]
print(num_list)
Selection(num_list,len(num_list))
print(num_list)