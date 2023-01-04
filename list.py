#1. Program to declare and print a list

# n=[78,6,645,4,5,6,4]
# print(n)

#2. Python program to print list elements in different ways
# n=[78,6,645,4,5,6,4]
# print(n)
# print(*n)
# print(*n,sep=',')

# 3. Program for Adding, removing elements in the list.
# n=[78,6,645,4,5,6,4]
# n.append(450)
# print(n)
# n.remove(6)
# print(n)

#4. Program to print a list using 'FOR and IN' loop.
# n=[78,6,645,4,5,6,4]
# for i in n:
#     print(i)


#5. Program to add an element at specified index in a list.
# n=[78,6,645,4,5,6,4]
# n.insert(1,99)
# print(n)

#6. Program to remove first occurrence of a given element in the list.
# n=[78,6,645,4,5,6,4]
# del n[2]   #needs check
# print(n)

#7. Remove all occurrences a given element from the list.

#8. Program to remove all elements in a range from the List.
# n=[78,6,645,4,5,6,4]
# print(n)
# del n[1:3]
# print(n)


#9. Program to Print the index of first matched element of a list
# n=[78,6,645,4,5,6,4]
# i=0
# while i<len(n):
#     j=i+1
#     while j<len(n):
#         if(n[i]==n[j]):
#             print(n.index(n[i]))
#             break
#         j+=1
#     i+=1   

#10. Convert a string to integers list
# n='falkata to going to school'.split()
# l=[i for i in n]
# print(l)     
            
#11. Input comma separated elements, convert into list and print
# n='falkata to going to school'.split()
# l=[i for i in n]
# print(*l)     

#12. Program to find the position of minimum and maximum elements of a list
# n=[78,6,645,4,5,6,4]
# big=n[0]
# for i in range(len(n)):
#     if(n[i]>big):
#         big=n[i]
# for i in range(len(n)):
#     if(n[i]==big):
#         print(n.index(n[i]))        

#13. Program to input, append and print the list elements.
# n=[78,6,645,4,5,6,4]
# n.append(65)
# print(n)

#14. Program to sort the elements of given list in Ascending and Descending Order.
# n=[78,6,645,4,5,6,4]
# print(n)
# i=0
# while i<len(n):
#     j=i+1
#     while(j<len(n)):
#         if(n[i]>n[j]):
#             b=n[i]
#             n[i]=n[j]
#             n[j]=b
#         j+=1
#     i+=1            
# print(n)

#15. Program to find the differences of two lists.
# a=[30,40,50,23,65,1,15]
# b=[30,40,60,15,65]
# l=[]
# for i in a:
#     if i not in b:
#         l.append(i)
# print(l)    
  

# 16. Program to Create two lists with EVEN numbers and ODD numbers from a list.
# n=[784,4,12,5,31,56,41,23]
# odd=[]
# even=[]
# i=0
# while i<len(n):
#     if(n[i]%2==0):
#         even.append(n[i])
#     else:
#         odd.append(n[i])
#     i+=1        
# print('even numbers:',even)
# print('odd numbers:',odd)            

#17. Program to print all numbers which are divisible by M and N in the List

# n=[623,12,45,21,42,32,450,40]
# x,y=map(int,input("emter your number:").split())
# i=0
# while i<len(n):
#     if((n[i]%x==0 )and(n[i]%y==0)):
#         print(n[i])
#     i+=1  

#18. Program to remove duplicate elements from the list. 
# n=[4,4,1,2,3,4,6,1,6,68,21]
# nl=[]
# i=0
# while i<len(n):
#     j=i+1
#     while j<len(n):
#         if(n[i]==n[j]):
#             n.pop(n[j])
#         j+=1
#     i+=1
# print(n)            

#19. Create a list from the specified start to end index of another list
# n=[4,6,20,5,4,4,4,1,52,458,51.201,541,125,5,51]
# star,end=map(int,input("enter your strat and  end input:").split())
# i=0
# nl=n[star:end]
# print(nl)

#20. print list after removing EVEN numbers.
# n=[10,2,6,1,6,12,3,14,17,19,54]
# i=0
# while i<len(n):
#     if(n[i]%2==0):   #not completed
#         n.pop(n[i])
#     i+=1
# print(n)        

#21. Iterate a list in reverse order.

#23. Create two lists with first half and second half elements of a list.
# n=[4,6,21,1,5,6,4,8,64,5,58,7,2]
# i=0
# st=[]
# sst=[]
# while i<len(n):
#     if(len(n)//2==0):
#         st=n[:len(n)//2]
#         sst=n[len(n)//2:]
#     else:
#         st=n[:len(n)//2] 
#         sst=n[len(n)//2:]   
#     i+=1    
# print(st)
# print(sst)

#24. print list after removing ODD numbers.
n=[4,54,11,2,3,44,98,7,66,11,17]
i=0
for i in n:
    if i%2!=0:
        n.remove(i)
print(n)        

