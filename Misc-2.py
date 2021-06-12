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