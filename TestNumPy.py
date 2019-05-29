import numpy as np
import pdb

list=np.arange(1,100,5)
print(list)

nums=[1,2,3,4,5,6]
sq_nums = []
for n in nums:
 sq_nums.append(n**2)

print(sq_nums)

sq_nums1 = []
sq_nums1= [n ** 2 for n in nums] # we could use a comprehension
print(sq_nums1)

#Type of list in numpy 
#array
#arange
#linspace
#logspace
#zeros
#ones

#Template:
#new_list = [f(x) for x in iterable]
words = ['hello', 'this', 'is', 'python']
caps = [word.upper() for word in words]
print(caps)

powers = [(x**2, x**3, x**4) for x in range(10)]
print(powers)
print(type(powers))
print(powers[1][2])

def isEven(num):
 return (num % 2 == 0)
myNum = 100
if isEven(myNum):
    print(str(myNum) + " is even")
numbers = [5, 18, 7, 9, 2, 4, 0]
#Template:
#new_list = [f(x) for x in iterable]

isEvens = [isEven(num) for num in numbers]
print(isEvens)

#pdb.set_trace()
