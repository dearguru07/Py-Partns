# n=5    
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=' ')
#     print()    


# n=5
# noc=n
# nor=n
# for i in range(1,n*2):
#     for j in range(1,n*2):
#         if noc==j or nor==j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()            
#     if i<n:
#         noc-=1
#         nor+=1
#     else:
#         noc+=1
#         nor-=1    


n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=' ')
    print()    