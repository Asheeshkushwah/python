# total__candies=10

# no_of_candies = int(input("no_of_candies:"))
# if no_of_candies in range(1,6):
#     print('no.of candies sold',no_of_candies)
#     print('number of candies available:',total__candies-no_of_candies)
# else:
#     print("invalid input")
#     print('no. of candies left:',total__candies)    




# a=int(input("enter the weight of clothes in gram:"))
# if(a==0):
#     print("time taken is 0 minute")
# elif(a<=2000):
#     print("time take is 20 minute")
# elif(a<=4000):
#     print("time take is 35 minute")
# else:
#     print("time take 45 minute")            




n =int(input("enter the value:"))
if n==0:
    print("time estimated : 0 minutes")
elif n in range(1,2001):
    print("time estimated :25 minutes")
elif n in range(2001,4001):
    print("time estimated :35 minutes")  
elif n in range(4001,7001):
    print("time estimated :45 minutes")
else:
    print("invalid input")         