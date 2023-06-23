# def fun(x):
#     print(x*2)
# fun (5)

# fun= lambda x : x*2
# print(fun(5))
# app = lambda x : x**3 + 4
# print(app(2))

# def appl(fx,value):
#     return 5 + fx(value)
# cube= lambda x: x*x*x
# print(appl(cube,4))

# def cube(x):
#     return x*x*x
# l=[2,4,6,8,20,54,99]
# lnew=[]
# for i in l:
#     lnew.append(cube(i))
# print(lnew)


# def cube(x):
#     return x*x*x
# l=[2,4,6,8,20,54,99]
# newl=list(map(cube,l))
# print(newl)

# cube = lambda x : x*x*x
# l=[2,4,6,8,20,54,99]
# newl=list(map(cube,l))
# print(newl)


##################
# def filter_function(a):
#     return a>10
# l=[2,4,6,8,20,54,99]
# newl=list(filter(filter_function,l))
# print(newl)

# ######OR
# filter_function= lambda a : a>10
# l=[2,4,6,8,20,54,99]
# newl=list(filter(filter_function,l))
# print(newl)

#######################
# from functools import reduce
# num=[1,2,3,4,5]
# sum=reduce(lambda x,y:x+y ,num)
# print(sum)

################################
# class Person:
#     name = "Ash"
#     occupation="None"
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a=Person()
# b=Person()
# c=Person()

# a.name="taha"
# a.occupation="none"
# b.name="adarsh"
# b.occupation="none"
# c.name="suj"
# c.occupation="none"

# a.info()
# b.info()
# c.info()

##########
################################
# class Person:
#     def __init__(self,name,occ):
#         print("Hey I am a developer.")
#         self.name=name
#         self.occ=occ
#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a=Person("Ash","CA")
# b=Person("XYZ","HR")

# a.info()
# b.info()



####################################
#GETTERS AND SETTERS
# class Myclass:
#     def __init__(self,value):
#         self._value=value
    
#     def show(self):
#         print(f"Value is {self._value}")
        
#     @property
#     def ten_value(self):
#         return 10* self._value
    
#     @ten_value.setter
#     def ten_value(self,new_value):
#         self._value = new_value/10
        
# obj=Myclass(10)
# obj.ten_value = 45
# print(obj.ten_value)
# obj.show()
##############################
#INHERITENCE
# class Employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
        
#     def show_details(self):
#         print(f"Details of Employee : {self.name}  & {self.id}")
        
# class Programmer(Employee):
#     def show_lang(self):
#         print("The default langauge is Python.")
        
# e1 = Employee("Ash" , 9)
# e1.show_details()

# e2 = Programmer("adarsh" , 45)
# e2.show_details()
# e2.show_lang()
###############################
#Access Modifiers
# class student:
#     def __init__(self):
#         self._name = "Ash"
        
#     def _funname(self):
#         return "AshPegesisss"
    
# class subject(student):
#     pass
# # obj=student()
# # obj1=subject()
# # print(obj)
# # print(obj)
# print(student()._name)
# print(subject()._funname())
##########################################
#STATIC METHOD :
# def add(a , b):  #replacable with @staticmethod
#         return a+b #replacable with @staticmethod
# class Math:
#     def __init__(self , num):
#         self.num = num
        
#     def showNum(self , n):
#         self.num = self.num  + n
        
    # @staticmethod
    # def add(a , b):
    #     return a+b
    
# a = Math(5)
# print(a.num)
# a.showNum(9)
# print(a.num)
        
############################################
#INSTANCE 
# class employee:
#     companyName="google"
#     NoOfEmployee=0
#     def __init__(self,name):
#         self.name = name
#         self.increment = '2%'
#         employee.NoOfEmployee+=1
#     def showDetails(self):
#         print(f"The details of employee are : {self.name}\nIncrement of Employee in {self.NoOfEmployee} sized company : {self.increment}\nCompany name : {self.companyName}"  )
        
# emp1=employee("Ash")
# emp1.increment = '5%'
# emp1.companyName="Microsoft"
# emp1.showDetails()

# emp2=employee("Adarsh")
# emp2.showDetails()
######################################
# print(1.53%10)


class employee:
    company = "Google"
    def show(self):
        
        print(f"The name is {self.name} and company is {self.company}")

    def newCompany(cls,newc):
        cls.company = newc

e1 = employee()
e1.name = "Adarsh"
e1.show()