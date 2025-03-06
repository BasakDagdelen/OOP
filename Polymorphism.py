class Add_Process:
    def calculate(self, a:int, b:int):
        return a + b
    
    
class Subtraction_Process:
    def calculate(self, a:int, b:int):
        return a - b


class Multiplication_Process:
    def calculate(self, a:int, b:int):
        return a * b
    
    
class Division_Process:
    def calculate(self, a:int, b:int):
        return a / b
 
    
class Mod_Process:
    def calculate(self, a:int, b:int):
        return a % b
    
    
def mathematical_process(process, a: int, b:int):
    return process.calculate(a,b)


add = Add_Process()
subtraction = Subtraction_Process()
multiplication = Multiplication_Process()
divison = Division_Process()
mod = Mod_Process()


print(f'Add: {mathematical_process(add, 15, 10)}')
print(f'Subtraction: {mathematical_process(subtraction, 12, 4)}')
print(f'Multiplication: {mathematical_process(multiplication, 3 , 7)}')
print(f'Divison: {mathematical_process(divison, 44, 6)}' )
print(f'Mod: {mathematical_process(mod, 79, 13)}')