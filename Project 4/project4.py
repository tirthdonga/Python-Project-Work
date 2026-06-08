arr = []

# __doc__
def display_docstring(func):
    """Prints the __doc__ of a given function to the console."""
    if func.__doc__:
        print("\n--------------------------------------------------")
        print(f"FUNCTION INFO: {func.__doc__.strip()}")
        print("--------------------------------------------------")

# case 1
# input 
def input_data_case():
  '''Prompts the user to either select preset sample data or manually input a space-separated 1D array.'''
  global arr
  print("\n--- Data Input Options ---")
  print("1. Use Sample Data")
  print("2. Use Manual Data Entry")
  
  choice_case1 = int(input("\nEnter Your Choice: "))
  match choice_case1:
    case 1: 
      arr = [3, 4, 1, 5, 8, 9, 6, 2, 7, 10]
      print("\n--------------------------------------------------")
      print(f"Stored Dataset: {arr}")
      print("Data Has Been Stored Successfully!")
      print("--------------------------------------------------")
    case _:
      print("\nEnter data for a 1D array (separated by spaces):")
      user_input = input()
      arr = []
      for i in user_input.split():
        arr.append(int(i))
      print("\n--------------------------------------------------")
      print("Data Has Been Stored Successfully!")
      print("--------------------------------------------------")
    
# case 2
# build in function use
def data_summary(*args, **kwargs):
    '''Computes and prints dataset summaries.'''
    if not args:
        print("\n--------------------------------------------------")
        print("🛑 Error: Dataset is empty.")
        print("--------------------------------------------------")
        return

    decimals = kwargs.get('precision', 2)

    total_element = len(args)
    min_value = min(args)
    max_value = max(args)
    sum_value = sum(args)
    ave_value = round(sum_value / total_element, decimals)

    print("\n--------------------------------------------------")
    print("                DATASET SUMMARY                   ")
    print("--------------------------------------------------")
    print(f"Total elements       : {total_element}")
    print(f"Minimum Value       : {min_value}")
    print(f"Maximum Value       : {max_value}")
    print(f"Sum Of All Values   : {sum_value}")
    print(f"Average Of All Values: {ave_value}")
    print("--------------------------------------------------")

# case 3
# Factorial Calculate (Recursive Architecture)
def factorial_case():
    '''Finds a targeted integer within the global dataset and calculates its mathematical factorial.'''
    global arr
    if not arr:
        print("\n--------------------------------------------------")
        print("🛑 Error: Dataset is empty. Please input data first (Option 1).")
        print("--------------------------------------------------")
        return

    def calculate_factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * calculate_factorial(n - 1)

    fac_num = int(input("\nEnter Number You Want Factorial Of: "))
    found = False
    
    print("\n--------------------------------------------------")
    for i in range(len(arr)):
        if fac_num == arr[i]:
            found = True
            fac_result = calculate_factorial(fac_num)
            print(f"Factorial of {fac_num} is: {fac_result}")
            break 
            
    if not found:
      print(f"🛑 Error: {fac_num} is not present in the dataset.")
    print("--------------------------------------------------")

# case 4
# Filter Data By Threshold
def filter_data_case(*args):
    '''Asks for a threshold and filters out values from the passed dataset elements.'''
    if not args:
        print("\n--------------------------------------------------")
        print("🛑 Error: Dataset is empty.")
        print("--------------------------------------------------")
        return

    threshold = int(input("\nEnter a threshold value to filter out data above this value: "))
    filtered_iterator = filter(lambda x: x >= threshold, args)
    filtered_result = list(filtered_iterator)
    
    print("\n--------------------------------------------------")
    print(f"Filtered Data (values >= {threshold}):")
    print(", ".join(map(str, filtered_result)))
    print("--------------------------------------------------")

# case 5
# Sort The Data
def sort_case():
  '''Queries the user for their sorting direction preference'''
  global arr
  if not arr:
        print("\n--------------------------------------------------")
        print("🛑 Error: Dataset is empty.")
        print("--------------------------------------------------")
        return
  
  print("\n--- Choose Sorting Order ---")
  print("1. Descending")
  print("2. Ascending")
  sort_choice = int(input("\nEnter Your Choice: "))

  match sort_choice:
    case 1:
      sort_order = True
      sort = "Descending"
    case _:
      sort_order = False
      sort = "Ascending"
  
  arr.sort(reverse=sort_order)
  print("\n--------------------------------------------------")
  print(f"Your Data Has Been Sorted in {sort} Order: ")
  print(", ".join(map(str, arr)))
  print("--------------------------------------------------")

# case 6
# Statistics Using UDF

def statistics_case(*args):
    '''Calculates and returns multiple dataset statistics'''
    if not args:
      return None

    temp_arr = sorted(args)
    minimum = temp_arr[0]
    maximum = temp_arr[-1]
    
    sum_val = 0
    for i in temp_arr:
      sum_val += i
        
    average = round(sum_val / len(temp_arr), 2)
    return minimum, maximum, sum_val, average
    
# case: 7
# Print Data set
def print_data_case():
    '''Printing Your Current Data Set Elements'''
    global arr
    if not arr:
      print("\n--------------------------------------------------")
      print("🛑 Error: Dataset is empty.")
      print("--------------------------------------------------")
    else:
      print(f"Current Data Set: {arr}")
#-----------------------------------------------------------------------------------------

while True:
  print("\n--------------------------------------------------")
  print("Welcome To Data Analyzer and Transformer Program")
  print("--------------------------------------------------")
  print("1. Input Data")
  print("2. Display Data Summary")
  print("3. Calculate Factorial")
  print("4. Filter Data By Threshold")
  print("5. Sort Data")
  print("6. Display Dataset Statistics")
  print("7. Print Your Data")
  print("0. Exit Program")
  print("--------------------------------------------------")

  choice = int(input("Enter Your Choice: "))

  match choice:
    case 1: 
      display_docstring(input_data_case)
      input_data_case()
    case 2: 
      display_docstring(data_summary)
      data_summary(*arr, precision=2)
    case 3:
      display_docstring(factorial_case)
      factorial_case()
    case 4: 
      display_docstring(filter_data_case)
      filter_data_case(*arr)
    case 5:
      display_docstring(sort_case)
      sort_case()
    case 6:
      display_docstring(statistics_case)
      stats_result = statistics_case(*arr)
      if stats_result is None:
          print("\n--------------------------------------------------")
          print("🛑 Error: Dataset is empty.")
          print("--------------------------------------------------")
      else:
          min_val, max_val, total_sum, avg_val = stats_result
          print("\n--------------------------------------------------")
          print("            DATASET STATISTICS BY UDF             ")
          print("--------------------------------------------------")
          print(f"- Minimum value: {min_val}")
          print(f"- Maximum value: {max_val}")
          print(f"- Sum of all values: {total_sum}") 
          print(f"- Average value: {avg_val}")
          print("--------------------------------------------------")
    case 7: 
      display_docstring(print_data_case)
      print_data_case()
    case 0:
      print("\n--------------------------------------------------")
      print("Exiting Program. Goodbye! 👋")
      print("--------------------------------------------------\n")
      break
    case _:
      print("\n--------------------------------------------------")
      print("🛑 You Entered An Invalid Choice")
      print("--------------------------------------------------")
