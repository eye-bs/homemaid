a = 1
print(a)

b = 'hello'
print(b)

if a == 1:
    print('hi')
elif a == 2:
    print('a is 2')
else:
    print('else!')

# check none use 'is'
if a is None:
    print('a is None')

if a:
    print('a')

if a is not None:
    print('a is not None')

def say():
     print('say hello')

def say1(number):
    print(f'hi {number}')

# not recommended
def say2(number: int):
    print('hi' + str(number))

say()
say1(3)