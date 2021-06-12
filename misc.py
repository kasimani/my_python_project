import os


def parrot_trouble(talking, hour):
    if (talking and (hour < 7 or hour > 20)):
        return True
    else:
        return False

talking = "True"
hour = 21
print(parrot_trouble(talking, hour))


def not_string(str):
    if len(str) >= 3 and str[:3] == "not":
        print("Printing as it is !!")
        print(str)
    else:
        print("not " + str)


str = "hixxxhi"
n = 1
#not_string(str)

def missing_char(str, n):
    front = str[:n]   # up to but not including n
    back = str[n+1:]  # n+1 through end of string
    return front + back

print(missing_char(str, n))


def front_back(str):
    if len(str) <= 1:
        return str

    mid = str[1:len(str)-1]
    return str[len(str)-1] + mid + str[0]

print(front_back(str))

print("=========================================")

def string_bits(str):
    result = ""
    # Many ways to do this. This uses the standard loop of i on every char,
    # and inside the loop skips the odd index values.
    for i in range(len(str)):
        #if i % 2 == 0:
         result = result + str[:i+1]
         print(result)
    return result


string_bits(str)
print("=========================================")
str = "ax3xaaxx"

def last2(str):
    #print(str)
    last2 = str[len(str)-2:]
    #print(last2)
    count = 0
    for i in range(len(str)-2):
        sub = str[i:i+2]
        print(i)
        print("Hellllllo --- " + str[i:i+2])
        #print("=======")
        #print(sub)
        if sub == last2:
            count = count + 1

    print(count)


last2(str)

print("========================Manish ================")
'''
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
'''


def array_front9(nums):
    if len(nums) < 4 and nums[:3] == 9:
        #print(len(nums))
        return False
    for num in nums[:4]:
        #print(num)
        if num == 9:
            return True
    return False


nums = [1, 1, 2, 3]
print(array_front9(nums))

print("========================Manish-2================")
'''
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
'''


def array123(nums):
    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

print(array123(nums))

print("========================Manish-2================")


animals = ['cat', 'dog','billi', 'pig', 'cow', 'duck', 'horse']

animals.sort(reverse=True)
print(animals)

print("========================Dictionary-2================")
dic_animals =  {'small':'cat','big':'horses', 'micro':'bacteria'}
for snort in sorted(dic_animals.keys()):
    print("Keys are: " + snort + " and Values are: ")

print("========================Misc-2================")

val22 = (60 + (10 ** 2) / 4 * 7)

print(val22)

print("========================Print-reverse-2================")
rev = 'hello'
print(rev[::-1])

nested_list = [3,1,[2,4,'Hello']]
print(nested_list)
nested_list[2][2] = 'GoodBye'
print(nested_list)

print("========================Print-Dict-2================")

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d['k1'][2]['k2'][1]['tough'][2][0])

print("========================Print-ForLoop ================")
a = [0,1,2,3,4,5,6,7,8,9]

for i in reversed(a):
    for z in range(0, i+1):
        print('*', end=" ")
    print("\r")

for i in range(0, 10):
    for z in range(0, i+1):
        print('*', end=" ")
    print("\r")

print("========================While - Print ================")
get_a = 0
while get_a < 20:
    for ii in reversed(a):
        for zz in range(0, ii+1):
            print('*', end=" ")
        print("\r")
    for i in range(0, 10):
        for z in range(0, i+1):
            print('*', end=" ")
        print("\r")
    get_a += 1


lisa = ['M','a','n','i','s','h']
lisa.reverse()
print(lisa)

'''
Break, Continue, Pass
Break : Breaks out of the current closest enclosing loop
Continue: Goes to the top of the closest enclosing loop
Pass: Does nothing at all, ignore Syntax error and let the program to pass that piece of Code.
'''

## Pass:
for i in range(0,10):
    pass


'''
for i in range(0,10):
    pass
'''

print("by-passing above piece of code even if there is syntax error")

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

print("\r")
#################################

word = 'abcde'
for index,letter in enumerate(word):
    print(index,letter)
    print("\r")


l1 = ["eat","sleep","repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)
print
# changing index and printing separately
for count,ele in enumerate(l1,100):
    print (count,ele)


cheeseList = ['Wensleydale', 'Stilton', 'Danish Blue', 'Red', 'Leicester', 'Brie']
for cheese in range(0, len(cheeseList)):
    print(f"Do you have some",cheeseList[cheese], "?")
    print("Not as such")



mystrin = 'Manish'

newlist = [x for x in mystrin]
print(newlist)

newlist1 = [y for y in 'Human']
print(newlist1)

newlist1 = [y**2 for y in range(0,11)]
print(newlist1)

newlist1 = [y for y in range(0,11) if y%2==0]
print(newlist1)


for x in [2,3,4]:
    for y in [10,100,1000]:
        print(x*y,end=" ")

print("\r")

s = "Print only the Sword that start with s in this sentence"

for word in s.split():
    if word[0].lower() == 's':
        print(word)
print("\r")
for num in range(0,10):
    if num%2 == 0:
        print(num)
print("\r")

for word in s.split():
    if len(word)%2 == 0:
        print(f'{len(word)} of {word} is Even !')
    else:
        print(f'{len(word)} of {word} is Odd ! ')

for num in range(1,101):
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num%3 == 0:
        print("Fizz")
    elif num%5 == 0:
        print("Buzz")
    else:
        print(num)


man = [1,2,3]

man.append(4)
print(man)
man.pop()
print(man)
man.index(1)
print(man.index(1))

print("Human")


def get_even_num(evennum):

    evennumbers = []

    for number in evennum:
        if number % 2 == 0:
            evennumbers.append(number)
        else:
            pass
    return evennumbers


numasas = [1,2,3,4,5,6,7,8]

print(get_even_num(numasas))

print("Human")


work_hours = [('Manish',100), ('Ankush',200), ('Raghav',300)]


def employee_check(get_details):
    hours_max = 0
    employee_name = ''
    for employee,hours in get_details:
        if hours > hours_max:
            hours_max = hours
            employee_name = employee
        else:
            pass
    return (employee_name,hours_max)


result = employee_check(work_hours)
print(result)
print("Human")


