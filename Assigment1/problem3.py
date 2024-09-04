one = 1,[20,30,40,50,60]
two = 2,[20,30]
three = 3,[20,30,40]
four = 4,[20,30,40,50,60,70]
five =5,[20,30,40,50,60,70,80]

dataset = [one,two,three,four,five]

def highest_average(dataset):
    dict_ = {}
    for data in dataset:
        if len(data[1])>=3:
            count = 0
            total_score = 0
            for i in data[1]:
                total_score+=1
                count+=1
            average_score = total_score/count
            dict_[data[0]] = average_score
    value1 = -100
    student = -1
    for key,value in dict_.items():
        if value>value1:
            value1 = value
            student = key
    return student


print(highest_average(dataset))



