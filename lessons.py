print ("Hello world line 1")
print ("Hello world line 2")

#------------------------------
# Переменные
#------------------------------

a=7 ; b=3 ; print (a+b)
f_name = "Alexey" ; l_name = "Ryabtsev" ; print ("Creator: "+ f_name + ' ' + l_name)

#------------------------------
# Строки
#------------------------------

name = "КрИвОй ТеКсТ"

print (name.title())
print (name.upper())
print (name.lower())

print  ("Какая-то строка\nЕще одна строка\n\nЧерез строку\n")
print  ("Какая-то строка\n\tЕще одна строка\n\tt значит таб \n")
print ("Lower name: " + f_name.lower())
#.rstrip() - стирает пробелы справа
#.lstrip() - стирает пробелы справа
#.strip() - стирает пробелы с двух сторон или ставим символы в ковычках какие подрезать .strip("")

#------------------------------
# Числа
#------------------------------

num1 = 10; num2 = 5; num3 = num2 + 15; print (num3); print (2+2*2)

#------------------------------
# Циклы (loops)
#------------------------------

for x in range(0,100,3): #(старт, конец, шаг)
    print ("number x = " + str(x))
    if x == 63:
        break
print ("-----EOF-----")

x=0
while True:
    print(x)
    x = x + 1
    if x == 7:
        break


print ("===========================")

cities = ['New York', 'Moscow', 'new dehli', 'Toronto']
print(cities)
print(len(cities))
print (cities[0]) #Первое значение
print (cities[-1]) #с конца
print (cities[2].upper())

cities [2] = 'Tula'
cities.append('minsk') #добавить в конец
cities.insert(2,'mogilev') #добавить куда надо
print(cities)


del cities[3] #Удалить под индексом 
print (cities)
cities.remove('Toronto')#Удалить по значению
print (cities)
deleted_city = cities.pop()
print("deeleted city is: " + deleted_city)
print (cities)

cities.sort(reverse=True) # Отсортировать (в обратном порядке)
print(cities)

cities.reverse()#Развернуть массив
print (cities)

print ("===========================")

cars = ['bmw', 'wolksvagen', 'seat', 'skoda', 'kia']
for x in cars:
    print (x.upper())

for x in range(1,6):
    print (x)

mynumber_list = list(range(0,10))
print(mynumber_list)
print ("==========")

for x in mynumber_list:
    x = x * 2
    print(x)
mynumber_list.sort(reverse=True)
print (mynumber_list)

print ("max number is: " + str(max(mynumber_list)))
print ("min number is: " + str(min(mynumber_list)))
print ("sum is: " + str(sum(mynumber_list)))
print("=======")

mycars = cars[1:4]
print (mycars)

mycars = cars[:4]
print (mycars)

mycars = cars[-3:]
print (mycars)

mycars = cars[:] #копирование массива для обработки в отличие от mycars=cars

print ("===========================")

#------------------------------
# Условия
#------------------------------


age=30
if age<=4:
    print("You are baby " + str(age) + " years old")
elif age>4 and age<12:
    print("You are kid " + str(age) + " years old")
elif age>=12 and age<19:
    print("You are teen " + str(age) + " years old")
else:
    print("You are old " + str(age) + " years old")

print("=========================")

all_cars = ['chrusler', 'dacia', 'bmw', 'KIA', 'VW', 'seat', 'skoda', 'lada', 'audi', 'ford', 'Chevrolett']
german_cars = ['bmw', 'VW', 'audi']

if 'lada' in all_cars:
    print("Yes, LADA is here")
else:
    print("No Lada here")

for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + " is German car")
    else:
        print(xxxx + " is not a German car")


    
#------------------------------
# Словари
#------------------------------

enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo',
    'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']
}

print("location X = " + str(enemy['loc_x']))
print("location Y = " + str(enemy['loc_y']))
print("His name is: " + enemy['name'])

enemy['rank'] = 'Admiral' #Добавить параметр
print (enemy)
del enemy['rank'] #удалить параметр
print (enemy)

enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] - 30
if enemy['health']<80:
    enemy['color'] = 'yellow'
print (enemy)

print(enemy.keys())
print(enemy.values())
print ("=================")

all_enemies = [] #Массив из десяти словарей
#all_enemies.append(enemy)
for x in range(0,10):
    all_enemies.append(enemy.copy())



all_enemies[5]['health'] = 30
all_enemies[8]['name'] = "Kozel"
all_enemies[2]['loc_x'] += 4

for ene in all_enemies:
    print(ene)


#------------------------------
# Ввод данных от пользователя
#------------------------------

#name = input("Please enter your name: ")
#print ("Your name is " + name)
#num11 = input ("enter X: ")
#num12 = input ("enter Y: ")
#sum = int(num11) + int(num12)
#print(sum)
#message = ""

#while message != 'sekret':
#    message = input("Enter Password ")
#    if message == "sekret":
#        break
#    print(message + "Password is not correct")
#print("Password was:" + message)

mylist = []
msg = ""
while msg != 'stop'.upper():
    msg = input("Enter new item, and STOP to finish ")
    mylist.append(msg)

print(mylist)