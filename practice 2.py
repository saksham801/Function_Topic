def animals(name, food, speed):
    return name, food, speed


print(animals('leopard', 'non veg', '303 km'))
# arguments = proccess of function offends dpends certain data provided to it while calling it this varabile calling in parnatheses call formal argu
# when function is called vlaue of each arguments must be provided those are the atucal arguments
# python default arguments = python allows to define a function with defulat value assign to one or more value  foraml args

def formal (name , age = 14):
    return  name, age

formal('leopard')


################################
# def formal2 (name , age , student , food , speed):
#     return name , age , student , food , speed
#
# name1000 = input('Enter your name: - ')  #harsh
# age1 = input('Enter your name: - ')  #harsh
# student2 = input('Enter your name: - ')  #harsh'
# food3 = input('Enter your name: - ')  #harsh
# speed4 = input('Enter your name: - ')  #harsh
# print(formal2(name1000 , age1 , student2 , food3 , speed4))
#
# # args = *args in python allows us to pass varible number of non keywords arguments to a pyhton a function in the function we should use * before the paramenter to pass a variable number of argument
#
#

def studnet(*student):
    print(student)

studnet('harsh' , 23 , 45)

# input ( 2 ,3 , 5,6 ) using *args
# output 2 + 3 + 5 + 6




# sum of number using loop in function through *args

def addition(*nums):
    count = 0
    for num in nums:
        #count = count + num
        count += num

    return count

print(addition(1,2,3,4,5,6,7,8,9))

