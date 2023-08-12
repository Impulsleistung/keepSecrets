# Let's test the black formatter with
""" def my_function(x,y): 
  if x> y:return y
  else:
     return x """

def my_function(x,y): 
  if x> y:return y
  else:
     return x

# It should become
""" def my_function(x, y):
    if x > y:
        return y
    else:
        return x """
