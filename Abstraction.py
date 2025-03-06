from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str, salary:float):
        self.name = name
        self.salary = salary
        
        
    @abstractmethod  
    def calculate_salary(self):
        pass
    
    
    
class FullTime_Employee(Employee):
    def __init__(self, name, salary):
         super().__init__(name, salary)
    
    def calculate_salary(self):
        return self.salary
    
    
    
class PartTime_Emloyee(Employee):
    def __init__(self, name, hourly_wage: int, working_hour: int ):
        super().__init__(name, hourly_wage * working_hour)
        self.hourly_wage = hourly_wage
        self.working_hour = working_hour
        
        
    def calculate_salary(self):
            return self.working_hour * self.hourly_wage
    
    
    
fulltime_employee = FullTime_Employee("Salih Dere", 55000)
parttime_employee = PartTime_Emloyee("Aslı Kaya", 1000, 25)
        
print(f"{fulltime_employee.name} maaşı: {fulltime_employee.calculate_salary()} TL")
print(f"{parttime_employee.name} maaşı: {parttime_employee.calculate_salary()} TL")
    