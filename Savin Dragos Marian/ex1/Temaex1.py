from employee import Employee

# Lungimea stringurilor 
X = len("Savin")
Y = len("DragosMarian")


class Manager(Employee):
    mgr_count = 0  # Variabila de clasa pentru numarul de obiecte Manager

    def __init__(self, name, salary, department):
        # Apelam constructorul clasei parinte
        super().__init__(name, salary)
        self.department = "F29 " + department
        Manager.mgr_count += 1

    def display_employee(self):
        if X % 3 == 0:
            print(f"Name: {self.name}")
        elif X % 3 == 1:
            print(f"Salary: {self.salary}")
        elif X % 3 == 2:
            print(f"Department: {self.department}")


# Crearea obiectelor Manager
managers = [Manager(f"manager{i + 1}", 10 * i+10, f"department{i + 1}") for i in range(Y // 3)]

# Afisam detalii pentru fiecare obiect Manager
print("Managers:")
for manager in managers:
    manager.display_employee()

print("-" * 40)

# Afisarea emp_count pentru instantele Employee si Manager
employee_instance = Employee("generic_employee", 5000)
manager_instance = managers[0]  # Un obiect Manager

print(f"Employee emp_count: {employee_instance.empCount}")
print(f"Manager emp_count: {manager_instance.empCount}")

# Afisam numarul total de Manageri
print(f"Number of Managers: {Manager.mgr_count}")
