one = dict(name="naga",courses={'a','b','c','d','e'},grades=dict(a=10,b=20,c=30,d=40,e=50))
two = dict(name="pranav",courses={'a','b','c'},grades=dict(a=10,b=20,c=30))
three = dict(name="naga",courses={'a','b'},grades=dict(a=10,b=20))

dataset = dict(s1 = one,s2=two,s3=three)

def highest_student(dataset):
    result_dic = {}
    for id,data in dataset.items():
        count = 0
        total_score = 0
        for i in data['grades'].values():
            count+=1
            total_score+=i
        average = total_score/count
        result_dic[id] = average
    key1 = 0
    value1 =0
    for key,value in result_dic.items():
        if value>value1:
            value1 = value
            key1 = key
    print(f"the student with highest average is {key1} with value {value1}")

highest_student(dataset)