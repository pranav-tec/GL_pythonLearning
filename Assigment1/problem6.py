one = (1,[('A',10),('B',20),('C',30)])
two = (2,[('A',10),('B',20)])
three = (3,[('A',10),('B',20),('C',30),('D',50)])

dataset = (one,two,three)

def highest_student(dataset):
    for data in dataset:
        result_dict ={}
        count = 0
        total_score = 0
        for data1 in data[1]:
            total_score+=data1[1]
            count+=1
        average = total_score/count
        result_dict[data[0]] = average

    key1 = 0
    value1 =0
    for key,value in result_dict.items():
        if value>value1:
            value1 = value
            key1 = key
    print(f"the student with highest average is {key1} with value {value1}")

highest_student(dataset)
highest_student(dataset)
