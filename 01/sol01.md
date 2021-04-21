```python
how_many_snakes = 5
snake_string = """
Welcome to Python3!
____
/ . .\\
\ ---<
\ /
__________/ /
-=:___________/
<3, Python
"""
print(snake_string * how_many_snakes)
```

    
    Welcome to Python3!
    ____
    / . .\
    \ ---<
    \ /
    __________/ /
    -=:___________/
    <3, Python
    
    Welcome to Python3!
    ____
    / . .\
    \ ---<
    \ /
    __________/ /
    -=:___________/
    <3, Python
    
    Welcome to Python3!
    ____
    / . .\
    \ ---<
    \ /
    __________/ /
    -=:___________/
    <3, Python
    
    Welcome to Python3!
    ____
    / . .\
    \ ---<
    \ /
    __________/ /
    -=:___________/
    <3, Python
    
    Welcome to Python3!
    ____
    / . .\
    \ ---<
    \ /
    __________/ /
    -=:___________/
    <3, Python
    



```python
#A 2.1
```


```python
Name = input("Enter your name")
Greatings = 'Stay Home Stay Safe ' +  ' ' + Name 
print(Greatings)
```

    Stay Home Stay Safe  Malik



```python
T_F_str = input('Enter Fahrenheit Temperature:')
T_F = float(T_F_str)
T_C = (T_F - 32.0) * 5.0 / 9.0
print (T_C) 
```

    36.666666666666664



```python
try: 
    T_F_str = input('Enter Fahrenheit Temperature:')
    T_F = float(T_F_str)
    T_C = (T_F - 32.0) * 5.0 / 9_0
    print (T_C) 
except: 
    print ('Only numeric input please') 
```

    Only numeric input please



```python
import math 
degrees = float(input('Enter Angle in Degrees:'))
radians = degrees / 360.0 * 2 * math.pi
print(radians)
print(math.sin(radians)) 
```

    3.141592653589793
    1.2246467991473532e-16



```python
#A 3.1
```


```python
for Counter in range(5):
    print(Counter)
```

    0
    1
    2
    3
    4



```python
for Counter in range(5,10):
    print(Counter)
```

    5
    6
    7
    8
    9



```python
for Counter in range(5,20,3):
    print(Counter)
```

    5
    8
    11
    14
    17



```python
for Counter in range(10,0,-2):
    print(Counter)
```

    10
    8
    6
    4
    2



```python
counter=7
while counter >=0:
    print(counter)
    counter-=2
print('Got it?')
```

    7
    5
    3
    1
    Got it?



```python
def IP(N):
    if (N < 2) or (N > 2 and N % 2 == 0):
        return False 
    for D in range(3,N - 1):
        if N % D == 0: 
            return False 
    return True 
```


```python
for n in range(2, 50):
    if IP(n) == True:
        print(n)
```

    2
    3
    5
    7
    11
    13
    17
    19
    23
    29
    31
    37
    41
    43
    47



```python
#P 1.1
```


```python
#Exercise 1
def checkPalindrome(num):
    return str(num)==str(num)[::-1]
```


```python
print(checkPalindrome(121))
print(checkPalindrome(1211))
```

    True
    False



```python
#Exercise 2
for i in range(5,0,-1):
    print(list(range(i,0,-1)))
#OR
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
```

    [5, 4, 3, 2, 1]
    [4, 3, 2, 1]
    [3, 2, 1]
    [2, 1]
    [1]
    5 4 3 2 1 
    4 3 2 1 
    3 2 1 
    2 1 
    1 



```python
#Exercise 3
def factorial(num):
    if num==0: return 1
    fac=1
    for i in range(abs(num),1,-1):
        fac*=i
    return fac*(abs(num)/num)
```


```python
print(factorial(5))
print(factorial(-5))
```

    120.0
    -120.0



```python
#P 1.2
```


```python
#Exercise 1
i=0
while i<=10:
    print(i,end=' ')
    i+=1
```

    0 1 2 3 4 5 6 7 8 9 10 


```python
#Exercise 2
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
divider=5

for x in list1:
    if x%divider==0: print(x,end=' ')
    if x>=150: break
```

    15 55 75 150 


```python
#Exercise 3
list1 = [10, 20, 30, 40, 50]
reverse=[]

#reverse = list[::-1]
#OR
for i in range(len(list1)-1,-1,-1):
    reverse.append(list1[i])
print(reverse)
```

    [50, 40, 30, 20, 10]



```python
#Exercise 4
start = 25
end = 50

isPrime = lambda num: all( num%i != 0 for i in range(2, int(num**.5)+1))
#OR
# def isPrime(num):
#     if num > 1:
#         for i in range(2, int(num**.5)+1):
#             if (num % i) == 0: return False
#         return True
#     return False

for i in range(start,end):
    if isPrime(i): print(i)

```

    29
    31
    37
    41
    43
    47



```python
#Exercise 5
numReverse = lambda num:int(str(num)[::-1])

print(numReverse(12315))
print(numReverse(53469))
```

    51321



```python
#Exercise 6
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(my_list)):
    if (i+1)%2==0: print(my_list[i])
```

    20
    40
    60
    80
    100



```python

```
