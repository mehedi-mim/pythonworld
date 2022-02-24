# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Employe:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first =first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@mim.com'
        Employe.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * Employe.raise_amount)
    #class methods as alternative constructors 
    @classmethod
    def set_raise_amt(cls,amount):
        print(f'{amount} {cls.raise_amount} : Mehedi Hasan Mim')
    
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
        
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        


# emp_1 = Employe('Mehedi','Mim',50000)
# emp_2 = Employe('Test','User',60000)

# print(emp_1.__dict__)
# emp_1.raise_amount = 1.05
# print(emp_1.__dict__)

# print(Employe.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(Employe.num_of_emps)

# Employe.set_raise_amt(20)
details = "Mehedi-Mim-10000"
new_obj = Employe.from_string(details)
print(new_obj.email)

import datetime
my_date = datetime.date(2022,2,22)

print(Employe.is_workday(my_date))
