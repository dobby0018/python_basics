x = "awesomewe"

def myfunc():
  global y
  y= "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + y)