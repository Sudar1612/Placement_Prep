ran=int(input())
odd=1
for row in range(1,ran+1):
    for col in range(1,odd+1):
        print("*",end=" ")
    odd+=2
    print()