#method to numbers between strings
a=77
cars=8
str="hello my name is abhinav and i am {} years old \nand i have {} cars"
print(str.format(a,cars))
str="hello my name is abhinav and i am {1} years old \nand i have {0} cars"
print(str.format(a,cars))