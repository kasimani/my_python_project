myfile = open('test.txt')
#print(myfile.read())
#print('0')
myfile.seek(0)
#print(myfile.read())
#print('-----------------------------------------')
myfile.seek(0)
myfile.close()

with open('test.txt') as myfile1:
    contents = myfile1.read()
#    print(contents)
    myfile1.close()

with open('test.txt',mode='a+') as myfile2:
    myfile2.write('Append\n')
   # print(myfile2)


readline = ""
print("Please enter your story")
while True:
    try:
        readline = input()
    except EOFError
        break
    with open('sasa.txt',mode='a+') as newfile:
        newfile.write(readline+'\n')

print("----------------------------------------------\n")
with open('sasa.txt', mode='r') as readfile:
    print(readfile.read())
    readfile.close()


