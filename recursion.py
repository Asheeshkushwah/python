#recursion
# def demo():
#     print("hello")
#     demo()
# demo()

#22

# n = int(input("enter the value of n:"))

# def natural(n):
#     if n==0:
#         return
#     print(n)
#     return natural(n-1) 
# natural(n)

#333
# def toy():
#     print('jain')
#     toy()
# toy()    



#444
# def num (n):
#     if(n<=0):
#         return
#     print(n,end="")
#     num(n-1) 

# def num1(n):
#     print(n,end="")
#     num(n-1)
# num1(10)  

# #555
def factorial(num):
    if num == 1 or num == 0:
        return num 
    return num *  factorial(num-1)  

number = int(input("enter a number:"))
result =factorial(number) 
print("factorial of:",result)   
