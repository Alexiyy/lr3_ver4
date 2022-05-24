def input_valid():
    pass

def x2(x):
    pass

def x3_1(x):
    pass

def collatz(x):
    while x != 1:
        if x % 2 == 0:
            return x2(x)
        else:
            return x3_1(x)
    print('Список имеет вид: ', sp)


sp = []
input_valid()