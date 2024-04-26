def naam(name):
    return name


print(naam(input("Enter your name: ")))


# harsh
def default(name, age=14, std=9):
    print('{}  {}  {}'.format(name, age, std))


default('HARSH')


# $ saksahm
def whises():
    for i in range(10):
        print("God Bless You")


whises()


# harsh
def wish():
    for i in range(10):
        print('happy birthday')


wish()


# saksham
def hi():
    print("{} ".format(input("Enter the  value:")))


hi()


#

def function1(name, age):
    return name, age


print(function1('harsh', 12))


def function1(*args):
    s = 0
    for i in range(10):
        s = s + i

    return s


print(function1(10, 12, 12))
