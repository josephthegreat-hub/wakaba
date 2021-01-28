class employee:
    name="joseph"
    def __init__(self, age, name, department, salary):
        self.age= age
        self.name= name
        self.department=department
        self.salary= salary
    def print_name(self):
        print(self.age)
    #def get_details(self):
        #s="{} is {} years old and works in {}  department and earns ksh {}".format(self.name, self.age, self.department, self.salary)
       # return s
        #return f"{ self.name} is {self.age} years old earns ksh{self.salary} works in {self.department}"
m1=employee(50, "joseph", "it", 10000)
m2=employee(34, "ann", "enginnering", 13400)
#print(m1.print_name())
#print(employee.name)
#print(employee.print_name())
#print(type(m1))
print(m2.salary)
#print(m2. get_details())