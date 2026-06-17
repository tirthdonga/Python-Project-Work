from datetime import datetime

class journalmanager:
  def __init__(self):
    self.__file_path = "Project 6/journal.txt"

  def entry(self):
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    entry = input("Enter Your Journal Entry: ")
    full_entry = f"[{timestamp}] {entry}"
    
    with open(self.__file_path, 'a') as file:
        file.write(full_entry + "\n")
    print(f"Entry saved at {timestamp}")


  def view(self):
    try:
      self.f = open(self.__file_path, 'r')
    except FileNotFoundError:
      print("File Not Found Error 🚫")
    else:
      print(self.f.read())
    finally:
      print("\nThis is All The Context In Journal\n")
  
  def search(self):
    word_to_search = input("Enter the word to search: ")
    print()
    
    line_number = 1
    found = False
    
    try:
      self.file = open(self.__file_path, "r")
    except FileNotFoundError:
      print("File Not Found Error 🚫")
    else:
      for line in self.file:
        if word_to_search in line:
          print(f"Found on line {line_number}: {line.strip()}")
          found = True
        line_number += 1
  
      if not found:
        print(f"No results found for '{word_to_search}'.")
    finally:
      print("\n")

  def clear(self):
    print("1. Confirm To Clear All Data")
    print("2. Go back")
    try:
      confirm = int(input("Enter Your Choice: "))
      if confirm == 1:
        with open("Project 6/journal.txt", 'w') as file:
          file.write("")
        print("Journal cleared successfully.")
      elif confirm == 2:
        print("Delete operation cancelled.")
      else:
        print("Invalid choice, operation cancelled.")
    except ValueError:
      print("Invalid input, please enter 1 or 2.")

obj = journalmanager()

while True:
  print("Welcome To Personal Journal Manager")
  print("Please Select Option\n")
  print("1. Add a New Entry")
  print("2. View All Entries")
  print("3. Search For Entry")
  print("4. Delete All Entries")
  print("0. Exit\n")

  choice = int(input("Enter Your Choice: "))
  print()

  match choice:
    case 1: 
      obj.entry()
    case 2:
      obj.view()
    case 3: 
      obj.search()
    case 4: 
      obj.clear()
    case 0: 
      break
    case _:
      print("\nInvalid Choice Entered 🚫")