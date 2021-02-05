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