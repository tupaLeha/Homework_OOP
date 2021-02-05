class Employee(object):
    name = 'Vasyan'
    mail = 'vasyan_228@mail.ru'
    salary = 40
    def work(self):
        return (self.name + ' has come to the office.')
    def chek_salary(self, days):
        return days * self.salary

work_employee = Employee()
work_employee.work()
class Recruiter(Employee):
    def work(self):
        return (self.name + ' has come to the office and start to hiring.')
    def __str__(self):
        return (self.__class__.__name__ + ':' + self.name)
class Programmer(Employee):
    def work(self):
        return (self.name + ' has come to the office and start to coding.')
    def __str__(self):
        return (self.__class__.__name__ + ':' + self.name)
work_Programmer = Programmer()
work_Recruiter = Recruiter()
print(str(work_Programmer))