def bubblesort(list2):
# Swap the elements to arrange in order
    for iter_num in range(len(list2)-1,0,-1):
        #print(iter_num)
        for idx in range(iter_num):
            #print(idx)
            if list2[idx]>list2[idx+1]:
                temp = list2[idx]
                #print(temp)
                list2[idx] = list2[idx+1]
                #print(list2[idx])
                list2[idx+1] = temp
                #print(list2)


list2 = [19,2,31,45,6,11,121,27]
bubblesort(list2)
print(list2)

#nested_list = [1,2,3]
#print(nested_list[1:])

my_dict = {'Item1':'Tata Tea', 'Item2':'Tata Salt', 'item3':[1,2,3]}
print(my_dict)
# Replace
my_dict['Item1'] = 'Tesla'
print(my_dict)
print(my_dict['item3'][2])
# Replace
my_dict['item3'][2] = 4
print(my_dict)
#Upper_Case
my_dict['Item2'] = my_dict['Item2'].upper()
print(my_dict)
# Print Keys only
print(my_dict.keys())
# Print Values Only
print(my_dict.values())
key2 = {'ker1':2,'ker2':5,'ker3':1,'ker4':6}
print(key2)
#Tupple and assign tuple to list
t = (1,2,1,'sa')
print(t.count(1))
print("Hello")
list_tupple = list(t)
print(list_tupple)
print(list_tupple[2])
list_tupple[0] = '3'
print(list_tupple)

print(set('Mississippi'))
print(set([1,1,2,3]))