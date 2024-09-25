import random


print("test")



def list_change(arr2):
    for i in range(len(arr2)):
        arr2[i] += 5


ar_verbs = ['hablar', 'cantar', 'bailar','trabajar','estudiar','caminar','escuchar','llevar','comprar','mirar']
ir_verbs = ['correr', 'vender', 'aprender','comprender','creer','romer','temer','comer','beber','comer']
er_verbs = ['vivir', 'escribir', 'abrir','recibir','comprartir','decidir','subir','insistir','permitir','existir']

print(ar)

arr = [0] * 5
print(arr)

"""
If you want to learn how to use real arrays, go here
https://www.w3schools.com/python/numpy/numpy_intro.asp


Whats the difference between an Array and List?
- To use an Array, you must import NumPy package
- Arrays can only store the same data type
- Arrays need to be declared
- Arrays are great for storing data more efficiently
- Arrays are great for numerical operations
    Such as I can divide the whole array by a number with a single operation
- Much faster to use than Lists



Lists - effectively you can think of them as ArrayLists from Java
- This is what Python uses traditionally  
- Lists don't need to be declared (Arrays do)
- Great to use if you have a short set of data, and don't use mathematical operations



Tuples - we wont use, but what are they?
- They are a collection which is unchangeable once created
- Indicate tuples by using ( ) instead of [ ]


"""
# Lists
arr = []
for i in range(10):
    arr.append(random.randint(1, 10))
print(arr)

# accessing individual data is the same, with the exception of
# negative indexing
# -1   --> access last data
# -2   --> access second to last data

print(arr[0])
print(arr[-2])

# you can access group of data using ranges
print(arr[2:4])  # 2 - 3
print(arr[2:])  # 2 - end
print(arr[:4])  # start - 3

# looping over lists is like for each

for element in arr:
    print(element)

# to access indexes
print(arr)
for i in range(len(arr)):
    print("index=", i, "element=", arr[i])
list_change(arr)
print(arr)

"""
append()    Adds an element at the end of the list
clear() Removes all the elements from the list
copy()  Returns a copy of the list
count() Returns the number of elements with the specified value
extend()    Add the elements of a list (or any iterable), to the end of the current list
index() Returns the index of the first element with the specified value
insert()    Adds an element at the specified position
pop()   Removes the element at the specified position
remove()    Removes the first item with the specified value
reverse()   Reverses the order of the list
sort()  Sorts the list
"""