def privet(x):
    if x == 0:
        return
    else:
        print("Hello world")
        privet(x-1)
privet(4)

print ("==========Сумма всех чисел====================")

def sum(a):
    if a == 0:
        return 0
    elif a ==1:
        return 1
    else:
        return a + sum(a-1)
z = sum(2)
print(z)

print ("==========Факториал====================")

def factorial(b):
    if b == 0:
        return 1
    else:
        return b * factorial(b-1)
print(factorial(5))

print ("==========Фибоначи===================")

def fido(m):
    if m == 0:
        return 0
    elif m==1:
        return 1
    else:
        return fido(m-1) + fido(m-2)
print(fido(10))

print ("==========Бинарный поиск===================")


def binarysearch(mylist, iskat, start, stop):
    if start > stop:
        return False
    else:
        mid = (start+stop) // 2
        if iskat == mylist[mid]:
            return mid
        elif iskat < mylist[mid]:
            return binarysearch(mylist, iskat, start, mid -1)
        else:
            return binarysearch(mylist, iskat, mid + 1, stop)


mylist = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]


iskat = 43

x = binarysearch(mylist, iskat, 0, len(mylist))
if x == False:
    print("Item ", iskat , " Not Found")
else:
    print("Item ", iskat , " Found at index ", x)
