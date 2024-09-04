one = 1,{'A','b','c','d'}
two = 2,{'a','b'}
three = 3,{'A','b'}
four = 4,{"d","f"}

print(type(four))

dataset = [one,two,three,four]

def get_students(dataset):
    lst = []
    for data in dataset:
        if len(data[1])==2:
            lst.append(data[0])
    return lst

print(get_students(dataset))