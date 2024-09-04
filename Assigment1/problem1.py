total_courses = ['A','B','C','D']
one = dict(studen_id = 1,name="naga",grades=[10,30,50,70],courses = ['A','B','C','D'])
two = dict(studen_id = 2,name="pranav",grades=[10,30,50],courses = ['A','B','C'])
three = dict(studen_id = 3,name="naga",grades=[10,30],courses = ['A','B'])
four = dict(studen_id = 4,name="pratheek",grades=[10,80,100,70],courses = ['A','B','C','D'])

dataset = [one,two,three,four]

print(dataset)
def get_average(dataset):
    total_score = 0
    count = 0
    for data in dataset:
        if len(data['grades'])==len(total_courses):
            count+=1
            for i in data['grades']:
                total_score+=i
    return total_score/count

print(get_average(dataset))
            
