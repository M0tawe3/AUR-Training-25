from random import randint

class Employee:
    def __init__(self, name, family, manager = None):
        self._name = name
        self._id = randint(1000, 9999)
        self._family = family
        self._manager = manager
        self.salary = 2500

    @property
    def id(self):
        return self._id
    
    @property
    def family(self):
        return str(self._family)
    
    def apply_raise(self, managed_employee: "Employee", raise_val: int):
        if managed_employee._manager != self:
            return False
        else:
            managed_employee.salary *= 1 + (raise_val / 100)
            print(f"New salary is {managed_employee.salary:.2f}")
            return True
        
if __name__ == '__main__':
    boss = Employee('Jane Redmond', {})
    name = 'John Smith'
    family = {
        'Son': {
            'Insured': True,
            'Age': 16
        },
        'Wife': {
            'Insured': False,
            'Age': 32
        }
    }
    my_employee = Employee(name,family, boss)
    not_boss= Employee('AdamCater', {})
    print(id(my_employee.family))
    print(id(my_employee._family))
    boss.apply_raise(my_employee,25)
    print(not_boss.apply_raise(my_employee, 25))