# try:
#     print(10/2)
# except Exception as e:
#     print("Error",e)
# finally:
#     print("finally block is executed")
# print("we are learining exception handling")



# def add(x,y):
#     if y==0:
#         raise Exception("y should not be zero")
#     return x/y
# try:
#     print(add(10,0))
# except Exception as e:
#     print("'error:",e)


def mul(x,y):
  if y==0:
    raise Exception("y not zero" )
  return x*y
print(mul(2,0))







