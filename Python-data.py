## Lists - Ordered sequences that can hold a variety of object types and mutable
list_val = [1,'string','20',29.30]
print(type(list_val))
print(list_val)
## Dictionary - Key and Value pair, unordered sequence mapping
dic_val = {'key1':'String', 'key2':10.20, 'key3':3}
print(type(dic_val))
print(dic_val)
## Tuple - Ordered sequnce of object and Immutable (vales can not be changed/reassigned)
tuple_val = ('huamn',2,4,3,2,19.20)
print(type(tuple_val))
print(tuple_val)
## sets - Unordered collections of unique elements, Cannot index, add or remove element possible
set_val = {"animal", 'human', 2, 3, 4, 5, 3, 1, 2,"animal"}
print(type(set_val))
set_val.add(19)
set_val.pop()
print(set_val)

'''
Break, Continue, Pass
Break : Breaks out of the current closest enclosing loop
Continue: Goes to the top of the closest enclosing loop
Pass: Does nothing at all, ignore Syntax error and let the program to pass that piece of Code.
'''

## Pass:
for i in range(0,10):
    pass

## Continue:
mystring = 'Manish'
for i in mystring:
    if i == 'a':
        continue
    print(i)


print("\r")
## Break:
for i in mystring:
    if i == 'i':
        break
    print(i)

