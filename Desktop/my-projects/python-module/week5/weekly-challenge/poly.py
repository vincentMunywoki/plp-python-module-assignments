class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary  # Private attribute

    def display(self):
        return f"{super().display()}, Salary: {self.__salary}"

    def change_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
        return f"Salary updated to {self.__salary}"

# Example usage
emp = Employee("John", 30, 50000)
print(emp.display())
emp.change_salary(55000)
print(emp.display())
