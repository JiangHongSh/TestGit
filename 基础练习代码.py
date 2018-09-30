Python 3.7.1rc1 (v3.7.1rc1:2064bcf6ce, Sep 26 2018, 15:15:36) [MSC v.1914 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('I\'m ok.')
I'm ok.
>>> print('I\'m learning\t Ptyhon')
I'm learning	 Ptyhon
>>> print('\\\t\\')
\	\
>>> print('\\\t\\')
\	\
>>> print(r'\\\n\\')
\\\n\\
>>> print('''line1
...line2
...line3''')
line1
...line2
...line3
>>> print('''line1
... line2
... line3''')
line1
... line2
... line3
>>> 
KeyboardInterrupt
>>> print('''line1
line2
line3''')
line1
line2
line3
>>> ture or false
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ture or false
NameError: name 'ture' is not defined
>>> Ture or False
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    Ture or False
NameError: name 'Ture' is not defined
>>> 5 > 3
True
>>> True or False
True
>>> a = 1
>>> t_007 = "T007"
>>> Answer = True
>>> a = "t007"
>>> print(a)
t007
>>> a = 'ABC'
>>> b = a
>>> a = 'XYZ'
>>> print(b)
ABC
>>> print(PI)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(PI)
NameError: name 'PI' is not defined
>>> 10/3
3.3333333333333335
>>> pi
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
>>> PI
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    PI
NameError: name 'PI' is not defined
>>> 9/3
3.0
>>> 10 // 3
3
>>> 10 / 3
3.3333333333333335
>>> 10 % 3
1
>>> 10 // 4
2
>>> ord('A')
65
>>> chr('20001')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    chr('20001')
TypeError: an integer is required (got type str)
>>> chr('23456')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    chr('23456')
TypeError: an integer is required (got type str)
>>> chr('25991')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    chr('25991')
TypeError: an integer is required (got type str)
>>> chr(12345)
'〹'
>>> chr(23456)
'宠'
>>> '\u4e2d\u6587'
'中文'
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> b'dadasasd中文'.decode('ascii',errors='ignore')
SyntaxError: bytes can only contain ASCII literal characters.
>>> b'dadasasd中文'.encode('ascii',errors='ignore')
SyntaxError: bytes can only contain ASCII literal characters.
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> b'dadasasd中文'.decode('ascii',errors='ignore')
SyntaxError: bytes can only contain ASCII literal characters.
>>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
'中'
>>> 'Hello, %s, you hava $%d.' %('mary',10000)
'Hello, mary, you hava $10000.'
>>> print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
SyntaxError: multiple statements found while compiling a single statement
>>> print('%2d-%02d' % (3, 1))
 3-01
>>> print('%.2f' % 3.1415926)
3.14
>>> 'growth rate: %d \%' %7
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    'growth rate: %d \%' %7
ValueError: incomplete format
>>> 'growth rate: %d %%' % 7
'growth rate: 7 %'
>>> classmates = ['1','2','3','4']
>>> classmates
['1', '2', '3', '4']
>>> classmates
['1', '2', '3', '4']
>>> len(classmates)
4
>>> classmates [0]
'1'
>>> classmates [-1]
'4'
>>> classmates [-2]
'3'
>>> classmates.pop()
'4'
>>> classmates
['1', '2', '3']
>>> classmate.pop(2)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    classmate.pop(2)
NameError: name 'classmate' is not defined
>>> classmates [2]
'3'
>>> classmate.pop(2)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    classmate.pop(2)
NameError: name 'classmate' is not defined
>>> classmate.pop(1)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    classmate.pop(1)
NameError: name 'classmate' is not defined
>>> classmates.pop(2)
'3'
>>> t = (1,2)
>>> t
(1, 2)
>>> age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
    
SyntaxError: multiple statements found while compiling a single statement
>>> age = 3
if age >= 18:
  print('your age is', age)
  print('adult')
else:
  print('your age is', age)
  print('teenager')
  
SyntaxError: multiple statements found while compiling a single statement
>>> names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
    
SyntaxError: multiple statements found while compiling a single statement
>>> names = ['Michael', 'Bob', 'Tracy']
>>> for name in names:
	print(name)

	
Michael
Bob
Tracy
>>> d.get('Thomas')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    d.get('Thomas')
NameError: name 'd' is not defined
>>> d.get('Thomas', -1)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    d.get('Thomas', -1)
NameError: name 'd' is not defined
>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d.get('Thomas', -1)
-1
>>> d.get('Thomas')
>>> def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

>>> print(my_abs(-99))
99
>>> import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
SyntaxError: multiple statements found while compiling a single statement
>>> def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

>>> x, y = move(100, 100, 60, math.pi / 6)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    x, y = move(100, 100, 60, math.pi / 6)
NameError: name 'math' is not defined
>>> def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

    
>>> enroll('Sarah', 'F')
name: Sarah
gender: F
age: 6
city: Beijing
>>> 
