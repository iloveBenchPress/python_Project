#a=5
#print(a,id(a))
#b=4
#print(b,id(b))
#a,b,c=1,2,3
#print(a)
#print("Документ\"file.txt\" \nнаходится по пути D:\\folder\\file.txt")
#s1="hello"
#s2="Python"
#print(s1+" "+s2)
"""
num = 4321  # 43
print(num)
a = num % 10
print("a:", a)
num = num // 10
# print(num)
b = num % 10
print("b:", b)
num = num // 10
# print(num)
c = num % 10
print("c:", c)
num = num // 10
# print(num)
d = num % 10
print("d:", d)
print(a * 1000 + b * 100 + c * 10 + d)

num=4321
print(num)
res=num%10*1000
num //=10
res+=num%10*100
num//=10
res+=num%10*10
num//=10
res+=num%10
print(res)
"""
import random

#num1="2"
#num2=3
#print(num1+str(num2))
#a=int(input("Введите первую сторону треугольника: "))
#b=int(input("Введите вторую сторону треугольника: "))
#c=int(input("Введите третью сторону треугольника: "))
#if a==b==c:
#    print("Треугольник равносторонний")
#elif a==b or a==c or b==c:
#    print("Треугольник равнобедренный")
#else:
#    print("Треугольник разносторонний")
'''
a=int(input("Введите номер месяца: "))
if 1<=a<=12:
    if 1<=a<=2 or a==12:
        print("Зима")
    if 3<=a<=5:
        print("Весна")
    if 6<=a<=8:
        print("Лето")
    if 9<=a<=11:
        print("Осень")
else:
    print("Ошибка ввода данных")

password="user"
match password:
    case "admin":
        print("Администратор")
    case "user":
        print("Пользователь")
    case _:
        print("Такого значения не существует")
day = "понедельник"
time = 10
match day:
    case "понедельник" | "вторник" | "среда" if 9<=time<=16:
        print("Рабочий день")
    case _:
        print("Такого дня недели не существует")
'''
#a,b=20,30
#minim=a if a<b else b
#print(minim)
#print("a==b" if a==b else "a>b" if a>b else "b>a")
"""
try:
    n=int(input("Введите целое число: "))
    print(n * 2)
except ValueError:
    print("Что-то пошло не так")

try:
    n = int(input("Введите делимое: "))
    m = int(input("Введите делитель: "))
    print(n/m)
except (ValueError, ZeroDivisionError):
    print("Нельзя вводить строки или нельзя делить на ноль")
else:#если в блоке try возникло исключение
    print("Всё нормально. Вы ввели числа",n,"и",m)
finally:
    print("Конец программы")

n=input("Введите первое число: ")
m=input("Введите второе число: ")
try:
    n=int(n)
    m=int(m)
except ValueError:
    n=str(n)
finally:
    print(n + m)

i=0
while i<=20:
    i += 1
    if i%2==0:
        print(i)

n=int(input("Введите начало диапазона: "))
m=int(input("Введите конец диапазона: "))
sum=0
while n<=m:
    if n%2!=0:
        sum+=n
    n+=1
print(sum)

i=0
while i<10:
    if i==3:
        i+=1
        continue
    print(i,end="")
    if i==5:
        break
    i+=1
print("\nЦикл завершён")


i = 1
while i<5:
    print("Внешний цикл: i =",i)
    j=1
    while j<4:
        print("\tВнутренний цикл j =", j)
        j+=1
    i+=1

i=1
while i<10:
    j=1
    while j<10:
        print(i,"*",j,"=",j*i,end="\t\t")
        j+=1
    print()
    i+=1

i=0
while i<3:
    j=0
    while j<6:
        print("^",end="")
        j+=1
    print()
    i+=1

i = 0
while i < 5:
    j = 0
    while j < 16:
        if j % 2 == 0:
            print("+", end="")
            j+=1
        else:
            print("-", end="")
            j+=1
    print()
    i+=1

i=0
while i<5:
    print(" " * i,"*")
    i+=1

a=int(input("Введите целое число: "))
for i in range(1,a):
    if a%i==0:
        print(i,end=" ")

w=int(input("Введите ширину прямоугольника: "))
h=int(input("Введите ширину прямоугольника: "))
for i in range(h):
    for j in range(w):
        if i==0 or i==h-1 or j==0 or j==w-1:
            print("*",end="")
        else:
            print(" ", end="")
    print()
"""
#d=[i for i in "Hello"]
#print(d)
#num= [i for i in range(30) if i % 2 == 0]
#print(num)
"""
nums=[8,3,9,4,1]
print(type(nums))
print(nums[0])


summ = 0
a = [int(input("->")) for i in range(int(input("n = ")))]
for i in range(len(a)):
    if a[i] < 0:
        summ += a[i]
print(summ)

s=list(range(10,101,10))
print(s)
for i in s:
    print(i,end=" ")

s=list(range(21,41))
print(s)
col=0
sum=0
for i in s:
    if i%2==0:
        col+=1
    else:
        sum+=i
print(col,sum)


a = [int(input("->")) for i in range(int(input("n = ")))]
print(a)
for i in range(1,len(a)):
    if a[i]>a[i-1]:
        print(a[i],end=" ")


a = [int(input("->")) for i in range(int(input("n = ")))]
print(a)
s=count=0
for i in range(len(a)):
    s +=a [i]
    if a[i]!=0:
        count +=1
print(s/count)


# print(s[::-1], id(s[::-1]))
# print(s[6:22], id(s[6:22]))
s= [9,5,6,3,7,4]
print(s)
s.append(8)
print(s)
s.extend([20,1,2])
s.extend("add")
print(s)
s.insert(3,100)
s.insert(20,222)
print(s)


a = [int(input("->")) for i in range(int(input("n = ")))]
print(a)
s=[]
n=int(input("Введите кол-во элементов списка:"))
for num in range(n):
    x=int(input("Введите кол-во элементов списка:"))
    s.append(x)
print(s)


s=[]
n=int(input("Кол-во элементов списка:"))

for num in range(n):
    x=int(input("Введите кол-во элементов списка:"))
    if x%3!=0:
        print(x,"не делится на 3 без остатка")
    else:
        s.append(x)
print(s)

a=[5,9,2,1,4,3,2,4]
b=[4,2,1,3,7]
c=[]
for i in a:
    for j in b:
        if i in c:
            continue
        if i == j:
            c.append(i)
            break
print(c)

s=[]
for el in a:
    if el in b and el not in s:
        s.append(el)
print(s)

a=[1,2,3]
b=[11,22,33,44,55]

c=[]
if len(b)>len(a):
    for i in range(len(a)):
        c.append(a[i])
        c.append(b[i])
    for i in range(len(a),len(b)):
        c.append(b[i])
else:
    for i in range(len(a)):
        c.append(a[i])
        c.append(b[i])
    for i in range(len(a), len(b)):
        c.append(b[i])
print(c)

a=[7,9,8,4,3]
last=a.pop(0)
print(a)

a=[7,9,8,4,3]
num=a.count(9)
print(num)
ind= a.index(4)
print(ind)

a=[1,2,3]
b=a.copy()
print(b)

a=[7,9,8,4,3]
print(a)
a.sort(reverse=True)
print(a)

s=["Виталий","Сергей","Александр","Анна"]
print(s)
s.sort(key=len,reverse=True)
print(s)
print(len())

a=[7,9,8,4,3]
print(a)
s=["Виталий","Сергей","Александр","Анна"]
print(s)
lst = sorted(s, key=len, reverse=True)
print(lst)
print(s)
"""
import random
"""
print(random.randint(1,4))
print(random.randrange(3,9,2))
print(round(random.uniform(10.5,25.5),2))

s=[20,30,40,50,60,70,80,90,10]
print(s)
#random.shuffle(s)
print(random.choice(s))
print(random.choices(s,k=3))

lst=[random.randint(0,100) for i in range(10)]
print(lst)

s=['20','30','40','50','60','70','80','90','10']
print(s)
print(sum(s))
print(max(s))
print(min(s))

s=[20,30,40,50,60,70,80,90,10]
print(s)
sum=0
for i in s:
    sum=sum+i
print(sum)


s=['20','30','40','50','60','70','80','90','10']
print(s)
print(len(s))
print(max(s))
print(min(s))

lst=[random.randint(0,100) for i in range(10)]
print(lst)
mux=max(lst)
print("Max:",mux)
lst.remove(mux)
lst.insert(0,mux)
print(lst)

x=list('1a2b3c4d')
print(x)
print('a' in x)
print('h' not in x)
s=input("Введите элемент: ")
if s in x:
    print("Такой элемент в списке есть")
else:
    print(s,"в списке отсутствует")


lst=[]
if not lst:#len(lst)==0:
    print("Список пустой")
print(bool(lst))



n1=int(input("Введите размер первого списка: "))
n2=int(input("Введите размер первого списка: "))
a=[random.randint(0,10)for i in range(n1)]
b=[random.randint(0,10)for j in range(n2)]
print("Первый список:",a)
print("Второй список:",b)
#c=a+b
#print(c)
c=[]
for i in range(len(a)):
    if a[i] not in c:
        c.append(a[i])
for i in range(len(b)):
    if b[i] not in c:
        c.append(b[i])
print(c)
c2=[]
for i2 in range(len(a)):
    if a[i2] in b and a[i] not in c2:
        c2.append(a[i2])
print(c2)
c3=[min(a),min(b),max(a),max(b)]
print(c3)


n1=10
s=[]
while len(s)!=n1:
    n=random.randrange(n1)
    if n not in s:
        s.append(n)
print(s)

m=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print(m)
#for row in range(len(m)):
#    #print(m[row])
#    for col in range(len(m[row])):
#        print(m[row][col],end= "\t\t")
#    print()
#print()

#for row in m:
#    for x in row:
#        print(x,end="\t\t")
#    print()
#print()

for row in m:
    for x in row:
        print(x**2,end="\t\t")
    print()
print()

w,h=5,3
matrix=[[random.randint(1,20) for x in range(w)]for y in range(h)]
#matrix=[[0 for x in range(w)]for y in range(h)]
for row in matrix:
    for x in row:
        print(x,end="\t\t")
    print()


#import math
from math import *
num1=sqrt(4)
num2=pi
num3=ceil(3.2)
num4=floor(3.2)
print(num1)
print(num3)
print(num4)

r=int(input("Введите радиус окружности: "))
print("Длина окружности:",round(2*pi*r,2))



import time
import locale
locale.setlocale(locale.LC_ALL,"ru")

#second = time.time()
#lt = time.ctime()
#lt2=time.localtime()
#print(second)
#print(lt)
#print(lt2)
#print("0" + str(lt2.tm_mday) if lt2.tm_mday<10 else lt2.tm_mday,".",lt2.tm_mon,".",lt2.tm_year,sep="")
#print(time.strftime("Today is %B %d, %Y"))
#print(time.strftime("%d/%m/%Y,%I:%M:%S"))
#print(time.strftime("Сегодня: %B %d, %Y"))

start = time.monotonic()
pause = 2
print("Программа запущена...")
time.sleep(pause)
print("Пауза была",pause,"секунд")
finish = time.monotonic()
res = finish - start
print(res)




def hello(name,age):
    print("Мне",age,"Меня зовут",name)


hello(17,"Sasha")


def get_sum(a,b):
    print("Сумма: ", end="")
    return a+b
    
n=2
m=5
res=get_sum(n,m)
print(res)
print(res + 5 - 2)
#c=3
#d=7
#get_sum(c,d)


def ch(a,b):
    if a>b:
        return a-b
    else:
        return a+b

print(ch(
    a=int(input("Ввудите a:")),
    b=int(input("Ввудите b:"))
))

def cub(a):
    return a*a*a


for i in range(1,11):
    print(i,"в кубе=",cub(i))


def change(lst):
    #lst[0],lst[-1]=lst[-1],lst[0]
    end=lst.pop()#удалили последний элемент из списка
    start = lst.pop(0)
    lst.insert(0,end)
    lst.append(start)
    return lst


print(change([1,2,3]))
print(change([9,12, 33, 54,105]))
print(change(['с','л','о','н']))


def maximum(one,two):
    if one>two:
        return True
    else:
        return False
print(maximum(9,6))
print(maximum(9,16))
if maximum(9,6):
    print("Первое число больше второго")
else:
    print("Второе число больше первого")



def chack_password(password):
    has_lower=False
    has_upper=False
    has_num=False
    for ch in password:
        if "a"<=ch<="z":
            has_lower=True
        if 'A'<=ch<="Z":
            has_upper=True    
        is '0'<=ch<='9':
            has_num=True
    if len(password)>=8 and has_lower and has_upper:
        return True
    return False

p=input("Введите пароль: ")
if chack_password(p):
    print("Надёжныё пароль")
else:
    print("Ненадёжныё пароль")


def get_sum(a,b,c,d):
    return a+b+c+d

print(get_sum(1,5,2,7))


def get_sum(a=1,b=2,c=4,d=5):
    return a+b+c+d

print(get_sum(c=3,d=8))


def set_param(c,s):
    print(s*c,end="")
set_param(8,"#")






def digit_sum(n,even=True):
    s = 0
    while n>0:
        cur_digit=n%10
        if even and cur_digit%2==0:
            s+=cur_digit
        if not even and cur_digit%2:
            s+=cur_digit
        n//=10

    return s
print("Сумма чётных цифр:")
print(digit_sum(9874023))
print(digit_sum(38271))
print(digit_sum(123456789))
print("Сумма нечётных цифр:")
print(digit_sum(9874023, even=False))
print(digit_sum(38271, even=False))
print(digit_sum(123456789, even=False))



def display_info(name,age):
    print("Name: ",name,"\nAge",age)


display_info("Sasha",17)

lt1=[1,2,3]
lt2=[1,2,3]
print(lt1==lt2)
print(lt1 is lt2)
print(id(lt1))
print(id(lt2))

a="Hello"
b="Hello"
print(a==b)
print(a is b)

a=a+"_new"
print(a)
print(id(a))
print(id(b))

a=[1,2]
print(a)
print(id(a),id(a[1]))
a[1]=3
print(a)
print(id(a),id(a[1]))

# Неизменяемые типы данных - int,str,float,bool, tuple(кортеж)
# Изменяемые типы данных - list,set,dict

lst=[10,20,30]
tpl=(10,20,30)
print(lst.__sizeof__())
print(tpl.__sizeof__())
print(tpl)


a=(1,5,9,7,8)
print(a,type(a))
b=tuple("Hello")
#b=tuple(["Hello","World"])
print(b,type(b))


a= 1,2,9,7,8
b=5,
print(a, type(a),type(b))


a=(5,9,7,3,4)
print(a[1:3])
print(a[-1])
print(a[4])


tpl=tuple([i for i in range(5)])
print(tpl)



tpl=tuple(2**i for i in range(1,13))
print(tpl)

t1=("hello")
t2=("world")
t3=t1+t2
sym="l"
try:
    print(t3.index(sym,4,-2))
except ValueError:
    print("Такого символа нет в заданном диапазоне")


def slicer(tpl,el):
    if el in tpl:
        if tpl.count(el)>1:
            first = tpl.index(el)
            second = tpl.index(el,first+1)+1
            return tpl[first:second]
        else:
            return tpl[tpl.index(el):]
    else:
        return tuple() # ()



print(slicer((1,2,3),8))
print(slicer((1,8,3,4,8,8,9,2),8))
print(slicer((1,2,8,5,1,2,9),8))

t=(10,11,[1,2,3],[4,5,6],["hello","world"])
print(t,id(t))
t[4][0]="hi"
t[4].append("new")
print(t,id(t))


t=(1,2,3)
#x=t[0]
#y=t[1]
#z=t[2]
x,y,z= t # распаковка кортежа
print(x,y,z)


def get_user():
    name = "Tom"
    age = 22
    is_married = False
    return name, age, is_married

user=get_user()
a,b,c=user
print(user,a,b,c)


d={0:'text',
   'one':45,
   (1,2.3):"кортеж",
   "список":[2,3,6,7],
   True:1,
   1:"Один",
   False:0}

key="one"
del d[key]




print(d)
print(d[(1,2.3)])
print(d[1],d[True])
print(d[0],d[False])

d['dva']='new ind'
print(d)

for key in d:
   print(key,":",d[key])
key2=1
try:
   del d[key2]
except KeyError:
   print("элемента нет в словаре")



sl={
   'x1':3,
   'x2':7,
   "x3":5,
   'x4':-1
}
a=1
for key in sl:
   a*=sl[key]
   print(sl[key])
print(a)

d={i:input("-> ")for i in range(1,5)}
print(d)
dislike=int(input("Какой элемент исключить: "))
del d[dislike]
print(d)


goods={
    '1':['Core-i3-4330',9,4500],
    '2':['Core-i5-4670',3,8500],
    '3':['AMD FX-6300',6,3700],
    '4':['Pentium G3220',8,2100],
    '5':['Core i5-3450',5,6400],
}

for i in goods:
    print(i,")",goods[i][0],"-",goods[i][1]," шт. по ",goods[i][2]," руб.",sep="")

while True:
    n=input("№: ")
    if n!="0":
        if n in goods:
            count = int(input("Количество: "))
            goods[n][1]=count
        else:
            print("Такого номера нет")
    else:
        break
for i in goods:
    print(i,")",goods[i][0],"-",goods[i][1]," шт. по ",goods[i][2]," руб.",sep="")


d={
    'a':1,
    'b':2,
    'c':3
}
print(d)
print(d.keys())
print(d.values())
print(d.items())

for key,value in d.items():
    print(key,"->",value)
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))




d={
    'a':1,
    'b':2,
    'c':3
}
#velue=d.get("b","Такого ключа нет")
#print(velue)
item=d.setdefault('w')
print(item)
print(d)



d={
    'a':1,
    'b':2,
    'c':3
}

item=d.pop('b')
print(item)


d={
    'a':1,
    'b':2,
    'c':3
}
item2 = d.popitem()
print(item2)

d=dict.fromkeys(['a','b'],100)
print(d)

d = {'a': 1, 'b': 2, 'c': 3}
d2 = [('r', 7), ('q', 9)]
# d2 = {'r': 7, 'q': 9}
# print(list(d2.items()))
# d.update(d2)
# d3 = d.copy()
# d3.update(d2)
d |= d2
print(d)


d={
    'name':"Kelly",
    'age':25,
    'salary':8000,
    'city':"New York"
}
new_d=dict()
new_d['name']=d.pop('name')
new_d['salary']=d.pop('salary')
print(d)
print(new_d)


d={
    'один':1,
    'два':2,
    'три':3,
    'четыре':4,
}

new_d={ key : value for key, value in d.items() if value <=2}
print(new_d)

a=('Dec','Jan','Feb')
b=(12, 1, 2)
c=(2.9,3.7,9.2)
#d=dict(zip(a, b))
d=list(zip(b,a,c))
print(d)

one = {
    'name': 'Igor',
    'surname':'Doe',
    'job':'Consultant'
}
two = {
    'name': 'Irina',
    'surname':'Smith',
    'job':'Manager'
}
for (k1, v1),(k2, v2) in zip(one.items(),two.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)


lt = [('Dec', 12), ('Jan', 1), ('Feb', 2)]
a,b = zip(*lt)
print(a)
print(b)


a=[1,2,3]
b=[4,*a,5,6]
print(b)
print(len(b))

first={'one':1,'two':2}
second={'three':3,'four':4,'one':11}
print({**first,**second})
for k,v in {**first,**second}.items():
    print(k,"=>",v)


colors=['red','green','blue']
i = 1
for color in colors:
    print(i,") ",color,sep="")
    i+=1
print()
for num, val in enumerate(colors,1):
    print(num, ") ", val, sep="")



studs={

}
sum=0
n=int(input('Количество студентов: '))
for i in range(n):
    name = input(str(i+1)+'-й студент: ')
    point=int(input('Балл: '))
    studs[name] = point
    sum+=point
    sr=sum//n
#sr=sum(studs.values())//n
print(studs)
print("Cредний балл: ",sr)
for i in studs:
    if sr<studs[i]:
        print(i)

def func(*args):
    return args
print(func(5))
print(func(5,6,7,8,'abc'))

def summa(*par):
    print(par)
    print(*par)
    res=0
    for n in par:
        res*=n
    return res
print(summa(1,2,3))
print(summa(1,2,3,4,5,6,7,8,9))

def ch(*args):
    avg = sum(args)/len(args)
    print(avg)
    res=[]
    for num in args:
        if num < avg:
            res.append(num)
    return res

print(ch(1,2,3,4,5,6,7,8,9))
print(ch(3,6,1,9,5))
s=1,2,3,4,5,6,7,8,9
print(type(s))
print(s)


def func(a,*args):
    return a, args
print(func(5))

def print_scares(student,*scores):
    print('Student name:',student,end=', Оценки: ')
    for score in scores:
        print(score,end=" ")
    print()

print_scares('johan',100,95,88,92,99,84)
print_scares('rick',96,20,33)

def func(**kwargs):
    return kwargs

print(func(a=1,b=2,c=3))

def intro(**data):
    for k,v in data.items():
        print(k,'is',v)
    print()

intro(name='Irina', sername = 'Sharma', age=22)
intro(name='Igor', sername = 'Wood', age=22,email='igor@mail.ru',country='Russia')


my_dict={'one':'first'}

def db(**kwargs):
    ...

print('my_dict =',my_dict)
db(k1=22,k2=31,k3=11,k4=91)
print('my_dict =',my_dict)
db(name='Bob',age=31,weight=61,eyes_color='grey')
print('my_dict =',my_dict)
"""


# def add(a):
#     x = 2
#
#     def outer():
#         #x = 3
#         print('x =',x)
#         return  a + x
#
#     return outer()
#
#
# print(add(5))

x = 25
t = 0
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#
#
#     inner()
#
#     print('a =',a)
#     t = a
#
# fn()
# c = x + t # 25 + 30 = 55 # 25 + 35 = 60
# print(c)

# def fn1():
#     x=25 # 2 # x = 55
#
#     def fn2():
#         # x = 33 # 4 # x = 55
#
#         def fn3():
#             nonlocal x
#             x = 55 # 6
#
#         fn3() # 5
#         print("fn2.x",x) # 7 # 33
#     fn2() # 3
#     print("fn1.x",x)  # 8 # 25
#
# fn1() # 1




# def outer(a1,b1,a2,b2):
#     a = 0
#     b = 0
#     def inner():
#         nonlocal a, b
#         a=a1+a2
#         b=b1+b2
#         print(a,b)
#     inner()
#
#     return [a,b]
#
# print(outer(2,3,-1,4)) # [1,7]


# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
# item1 = outer(5)
# print(item1(10))
#
# item2 = outer(6)
# print(item2(10))
#
# # print(outer(7)(10))

# c = [1,2,3]
# a = 1
# def func1():
#
#     b = 'line'
#
#
#     def func2():
#         # nonlocal a
#         nonlocal b
#         global a
#         c.append(4)
#         a = a + 1 # a+=1
#         b = b + '_new'
#         return a, b, c
#
#     return func2
#
# func = func1()
# print(func())


# def func(city):
#     #count = 0
#     def inner():
#         # nonlocal count
#         count =0
#         count +=1
#         print(city, count)
#
#     return inner
#
# res1 = func('Москва')
# res1()
# res1()
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res2()
# res1()


# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
# for t in c:
#     print(t("abc_"))



# def inc1(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
# func = inc1(10)
# print(func(5))
#
#
# def inc2(n):
#     return lambda x: n + x
#
# fun2 = inc2(10)
# print(func(5))
#
#
# inc3 = (lambda n: (lambda x: n + x))
#
# func3 = inc3(10)
# print(func3(5))

#print((lambda n: (lambda x: (lambda z: n + x + z)))(10)(5)(1))

# def func(i):
#     return i[1]
#
# d= {'a': 15, 'c': 10, 'b': 5}
# # lst = sorted(d.items(), key =lambda i: i[1])
# lst = list(d.items())
# # print(lst)
# # lst.sort(key=lambda i: i[1])
# lst.sort(key=func)
# print(lst)
# print(dict(lst))

# players = [
#     {'name': 'Антон','last_name': "Бирюков", "rating": 9},
#     {'name': 'Алексей','last_name': "Бодня", "rating": 10},
#     {'name': 'Фёдор','last_name': "Сидоров", "rating": 4},
#     {'name': 'Михаил','last_name': "Семёнов", "rating": 6},
# ]
#
# res = sorted(players, key=lambda item: item["last_name"])
# print(res)
#
# res1 = sorted(players, key=lambda item: item["rating"],reverse=True)
# print(res1)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y,lambda x, y: x / y]
# print(a[1](8,3))
# print(a[0](8,3))

# d={
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье"),
# }
#
# d[6]()

# from math import pi
#
# area = {
#     "Circle": lambda radius: pi * radius * radius,
#     "Rectangle": lambda a, b: a * b,
#     "Trapezoid": lambda a, b, h: (a + b) * h / 2
# }
# print("Площадь окружности:",area['Circle'](2))
# print("Площадь прямоугольника:",area['Rectangle'](10,13))
# print("Площадь трапеции:",area['Trapezoid'](7,5,3))

# print((lambda a, b: a if a > b else b)(5, 10))

# def outer(a,b,c):
#     def inner(i,j):
#         return i * j
#     s = 2 * (inner(a, b) + inner(a, c)+ inner(b,c))
#     return s
#
#
# print(outer(2,4,6))
# print(outer(5,8,2))
# print(outer(1,6,8))


# # s - стала глобальной переменной
# def outer(a,b,c):
#     def inner(i,j):
#         return i * j
#     s = 2 * (inner(a, b) + inner(a, c)+ inner(b,c))
#     return s
#
# outer(2,4,6)
# print(s)
# outer(5,8,2)
# print(s)
# outer(1,6,8)
# print(s)


# # нелокальная переменная
# def outer(a,b,c):
#     s = 0
#     def inner(i,j):
#         nonlocal s
#         return i * j
#     s = 2 * (inner(a, b) + inner(a, c)+ inner(b,c))
#     return s
#
# print(outer(2,4,6))
# print(outer(5,8,2))
# print(outer(1,6,8))


# работа с git
# git init
# - создаём репозиторий
# git status - проверка статуса
# git add -A или --all - все файлы, которые находятся в папках
# git config --global user.name 'моё имя'
#            --local
# git config --global user.email 'моя почта'
#
#
# git commit -m 'first commit' - контрольная точка репозитория



# print("Вносим изменения в GitHub ))")
# print("Внёс изменения")
print("Hello")
print('Hi')