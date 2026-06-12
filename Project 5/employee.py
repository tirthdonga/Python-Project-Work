class Person:
  per_name = None
  per_age = 0

  def per_setter(self):
    self.per_name = input("\nName: ")
    self.per_age = int(input("Age: "))

  def per_getter(self):
    print(f"Name : {self.per_name} | Age : {self.per_age}")

class employee:
  def __init__(self, name="", age=0, id=0, salary=0):
    self.__id = 0
    self.name = None
    self.age = 0
    self.__salary = 0

  def __del__(self):
    print(f"[System] {self.name} Data Has Been Cleared 🧹.")

  def setter(self):
    self.name = input("\nName: ")
    self.age = int(input("Age: "))
    self.__id = int(input("ID: "))
    self.__salary = int(input("Salary: "))

  def display(self):
    print(f"\nName: {self.name} | Age: {self.age} | ID: {self.__id} | Salary: {self.__salary}", end=" ")

class manager(employee):
  def __init__(self):
    super().__init__()
    self.department = None

  def setter(self):
    super().setter()
    self.department = input("Department: ")
  
  def display(self):
    super().display()
    print(f"| Department: {self.department}\n")

class developer(employee):
  def __init__(self):
    super().__init__()
    self.programming_language = None

  def setter(self):
    super().setter()
    self.programming_language = input("Programming Language: ")
  
  def display(self):
    super().display()
    print(f"| Language: {self.programming_language}\n")

person_list = []
employee_list = []
manager_list = []
developer_list = []

while True:
    print("\nEmployee Management System")
    print("\n1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. Create Developer")
    print("5. Display Details")
    print("6. Check Subclass")
    print("0. Exit\n")
    choice = int(input("Enter Your Choice: "))

    match choice:
        case 1:
          new_person = Person()
          new_person.per_setter()
          person_list.append(new_person)
        case 2:
          emp_obj = employee()
          emp_obj.setter()
          employee_list.append(emp_obj)
        case 3:
          man_obj = manager()
          man_obj.setter()
          manager_list.append(man_obj)
        case 4:
          dev_obj = developer()
          dev_obj.setter()
          developer_list.append(dev_obj)
        case 5:
          while True:
            print("\n1. Print Person")
            print("2. Print Employee")
            print("3. Print Mangaer")
            print("4. Print Developer")
            print("0. Exit")

            display_choice = int(input("\nEnter Your Choice: "))
            match display_choice:
              case 1:
                for p in person_list:
                    p.per_getter()
              case 2:
                for e in employee_list:
                    e.display()
              case 3:
                for m in manager_list:
                    m.display()
              case 4:
                for d in developer_list:
                    d.display()
              case 0:
                break
              case _:
                print("\nInvalid Choice, Please Try Again.🚫")
        case 6:
          print("\n--- Checking Subclass ---")
          print(f"Is 'Person' A Subclass Of 'Employee' : {issubclass(Person, employee)}")
          print(f"Is 'Manager' A subclass of 'Employee' : {issubclass(manager, employee)}")
          print(f"Is 'Developer' A subclass of 'Employee' : {issubclass(developer, employee)}")
        case 0:
          print("\nGood Bye👋👋\n")
          break
        case _:
          print("\nInvalid Choice, Please Try Again.🚫")