list=[]
i=1
desired_type=int
while i:
    try:
        num=int(input("enter the element: "))
        list.append(num)
    except ValueError:
        print("enter the correct integer type")
    option=input("wanna continue?(0/1)")
    if int(option):
        continue
    else:
        break
print(f"the list: {list}")
