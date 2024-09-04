one = dict(students=[1,3,2,4,5,6],grades = {30,50,30,60,80,100})
two = dict(students=[1,3,2,4,5,6,7,8],grades = {30,50,30,60,80,100,99,98})
three = dict(students=[1,3,2,4,5],grades = {30,50,30,60,80})

dataset = dict(A=one,B=two,C=three)

# print(dataset)

def highest_and_average(dataset):
    result_dic = {}
    for sub,dic in dataset.items():
        count = 0
        total = 0
        for i in dic['grades']:
            count+=1
            total+=i
        average = total/count
        result_dic[sub] = average
    for key,value in  result_dic.items():
        print(f"the average of subject {key} : {value}")
    key1 = 0
    value1 =0
    for key,value in result_dic.items():
        if value>value1:
            value1 = value
            key1 = key
    print(f"the subject with highest average is {key1} with value {value1}")

highest_and_average(dataset)