from abc import ABC

class polygon(ABC):
    def sides(self):
        pass

class app1():
    def __init__(self,gender):
        self.gender = gender
    
    def get_gender(self):
        return self.gender


class app(app1,polygon):
    count = 0 #data abstraction
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        super().__init__(gender)
        app.count = app.count+1


    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    #def sides(self):
        #print("the number of sides is 4")
    
if __name__ == "__main__":
    s = app("naga",23,"Male")
    p = app("pranav",24,"Male")
    print(s.get_name())
    print(s.get_age())
    print(s.get_gender())
    s.sides()
    a = 32
    b= False
    c = 33.456
    d = "Naga"
    e ='M'
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(s.count)
    print(2**3)
    print(2//3)

    k = 4
    l = 5
    # bitwise opeators
    print(k&l)
    print(k|l)
    print(~k)
    print(k^l)
    shift = k<<2
    print("shift",shift)
    shift1 = k>>2
    print("shift1",shift1)

    arr = [1,4,7,9]
    print(9 in arr)
    print(9 not in arr)

    print(k is l)
    print(k is not l)

    if(k^l):
        print("logic passd")
    
    print("value of k", k,"value of l:", l)
    print(f"value of k: {k} , value of l:{l}")
    print("value of k: {} , value of l:{}".format(k,l))
    print("numpy","pandas","matplotlib",sep=", ",end = "\n")
    print(k!=l)
    f = 17
    j = f<<2
    z = f>>2
    print(j)
    print(z)
    arr.remove(4)
    print(arr)
    set0 = {"mon","Tue","wed","thu","Fri","sat"}
    print(type(set0))
    for i in set0:
        print(i)
    set1 = {1,4,6,"Naga",50.6}
    print(type(set1))
    try:
        set2 = {4,56,[4,6,]} # set does not accept mutable elements lists,dictionaries and sets
        print(set2)
    except Exception as e:
        print(e)
    set3 = {4,6,(4,5)}
    print(type(set3))    
    set4 = set() #we cannot use {} since it represents dictionary
    set5 = {}
    print(type(set4))
    print(type(set5))
    set0.add("Sun")
    set0.add("Jan")
    print(set0)
    set0.update(["Feb","Mar","Dec"])
    print(set0)
    set0.discard("Dec")# if element is not present it does not raise error
    set0.remove("Feb")# it raises erro if element is not present
    print(set0)
    set0.pop()
    print(set0)
    set1.clear()
    print(set1)
    print(set0|set3)
    print(set3.union(set0))
    print(set0&set3)
    print(set0.intersection(set3))
    print(set0.union(set1,set3))

    days1 = {"monday","tuesday","wednesday"}
    days2 = {"monday","tuesday","Friday"}
    days3 = {"monday","tuesday","wednesday"}
    days4 = {"monday","tuesday"}
    print(days1-days2)
    print(days1.difference(days2))
    print(days1^days2)# ele
    print(days1.symmetric_difference(days2))
    print(days1==days3)
    print(days1>days4)# days1 is superset of days4
    print(days1.issuperset(days4))
    print(days4<days2)# days4 is subset of days2
    print(days4.issubset(days2))
    set6 = set([1,2,3,4])
    set7 = frozenset([3,5,6]) # it is immutable we can performall the actions that do not change the set
    print(type(set7))
    dict0 = {"nag":"pranav","pranav":"chakilam"}
    set8 = frozenset(dict0)
    print(set8)
    days8 = days1.copy()
    print(days8)

    dict1 = dict({(1,"naga"),(2,"pranav")})
    print(dict1)
    print(type(dict1))
    dict2 = {1:"chakilam",2:"pranav"}
    print(type(dict2))
    for x in dict2:
        print(x)
    for x in dict2.items():
        print(x)
    for x in dict2.keys():
        print(x)
    for x in dict2.values():
        print(x)
    dict1.pop(1)
    print(dict1)
    dict1[3]="srinivas"
    print(dict1)
    dict1.update({4:"nag",6:"chak"})
    print(dict1)
    print(dict1.get(6))
    dict1.popitem()
    print(dict1)
    dict1.clear()
    print(dict1)
    dict4 = dict2.copy()
    print(dict4)
    del dict4[1]
    print(dict4)
    print(len(dict4))
    print(sorted(dict0))
    def square(*args):
        square = []
        for i in args:
            square.append(i.upper())
        return square
    def square1(**kwargs):
        for key,value in kwargs.items():
            print("%s -> %s"%(key,value))
    print(square("naga","pranav"))
    square1(c="naga",second="pranav")
    