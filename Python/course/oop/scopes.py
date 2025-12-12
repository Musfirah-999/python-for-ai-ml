# x = 10

# def outer_function():
#   y=10
#   def inner_function():
#         z=10
#         print(f"Inner function z={z}")
#         print(f"Inner function y={y}")
#         print(f"Inner function x={x}")
#   inner_function()
#   print(f"Outer function y={y}")
#   print(f"Outer function x={x}")
# outer_function()
        
# a = 10

# def modify_a():
#     global a
#     a = 20
# print(a)
# modify_a()
# print(a)

x = 10

def outer_function():
  
  x=20
  def inner_function():
      nonlocal x
      x=30
        
  inner_function()
  print(x)
  
print(x)
outer_function()
print(x)


