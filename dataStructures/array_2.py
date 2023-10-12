#want to accept elements in array
list=[]
a=int(input("enter the number of elements:"))
for i in range(a):
    num=int(input(f"enter element{i}:"))
    list.append(i)
    
print(f"the list:{list}")

list_2=[x*10 for x in range(1,8)]
print(f"the list:{list_2}")