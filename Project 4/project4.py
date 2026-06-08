arr1 = []
arr2 = []
arr_dim = None

def sample_1d():
    """Loads a predefined sample 1D array."""
    global arr1, arr_dim
    arr1 = [10, 3, 7, 32, 21, 76, 80, 110, 6]
    arr_dim = "1d"

def manual_1d(input_string):
    """Converts a space-separated string into a 1D array."""
    global arr1, arr_dim
    arr1 = []
    for i in input_string.split():
        arr1.append(int(i))
    arr_dim = "1d"

def sample_2d():
    """Loads a predefined sample 2D matrix."""
    global arr2, arr_dim
    arr2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    arr_dim = "2d"

def manual_2d(rows):
    """Prompts user to input data for a 2D matrix row by row."""
    global arr2, arr_dim
    arr2 = []
    print("\nEnter each row's numbers separated by spaces:")
    for i in range(rows):
        row_input = input(f"Row {i + 1}: ")
        row = []
        for x in row_input.split():
            row.append(int(x))
        arr2.append(row)
    arr_dim = "2d"

def maximum():
    """Returns the maximum value found in the 2D matrix."""
    Max = arr2[0][0]
    for row in arr2:
        for ele in row:
            if ele > Max:
                Max = ele
    return Max

def minimum():
    """Returns the minimum value found in the 2D matrix."""
    Min = arr2[0][0]
    for row in arr2:
        for ele in row:
            if ele < Min:
                Min = ele
    return Min

def total_sum():
    """Calculates the sum of all elements in the 2D matrix."""
    Sum = 0
    for row in arr2:
        for ele in row:
            Sum += ele
    return Sum

def average():
    """Calculates the average of all elements in the 2D matrix."""
    Sum = 0
    NoOfElement = 0
    for row in arr2:
        for ele in row:
            Sum += ele
            NoOfElement += 1
    return Sum / NoOfElement

def data_stat(*args,**kwargs):
  """Returns min, max, sum, and average of the active dataset."""
  if args:
      print(f"\n--- {args[0]} ---")
  
  if arr_dim == "1d":
      min_val = min(arr1)
      max_val = max(arr1)
      sum_val = sum(arr1)
      avg_val = sum_val / len(arr1)
  else:
      min_val = minimum()
      max_val = maximum()
      sum_val = total_sum()
      avg_val = average()
    
  precision = kwargs.get('precision', 2)
  return min_val, max_val, sum_val, round(avg_val, precision)

def factorial(n):
    """Calculates the factorial of a number using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("\n" + "Welcome to Data Analyzer and Transformer Program".center(90, "-"))

while True:
    print("\nSelect from the menu which operation you want to use:\n")
    print("1. Insert Data as an array")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data By Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("0. Exit Program")
    
    choice = int(input('\nEnter your choice: '))
    
    match choice:
        case 1:
          print("\n--- Array Type Options ---")
          print("1. 1D Array")
          print("2. 2D Array")
          dimension_choice = int(input("\nEnter Your Choice (1 or 2): "))
          match dimension_choice:
              case 1:
                  choice_source = int(input("\n1. Sample Data\n2. Manual Data\nEnter choice: "))
                  if choice_source == 1:
                      sample_1d()
                      print(sample_1d.__doc__)
                  else:
                      manual_1d(input("Enter numbers: "))
                      print(manual_1d.__doc__)
              case 2:
                  choice_source = int(input("\n1. Sample Data\n2. Manual Data\nEnter choice: "))
                  if choice_source == 1:
                      sample_2d()
                      print(sample_2d.__doc__)
                  else:
                      manual_2d(int(input("Enter row size: ")))
                      print(manual_2d.__doc__)
              
              case _:
                print("\nInvalid Choice")
        case 2:
            if arr_dim == None:
                print("\nFirst insert an array.")
                continue
            print(f"\nInfo: {'Displays basic data summary (min, max, sum, avg).'}")
            if arr_dim == "1d":
                print(f"Total elements: {len(arr1)}")
                print(f"Minimum value : {min(arr1)}")
                print(f"Maximum value : {max(arr1)}")
                print(f"Sum of all values : {sum(arr1)}")
                print("Average value: %.2f" % (sum(arr1) / len(arr1)))
            else:
                print(f"Total elements: {len(arr2) * len(arr2[0])}")
                print(f"Minimum value : {minimum()}")
                print(f"Maximum value : {maximum()}")
                print(f"Sum of all values : {total_sum()}")
                print("Average value: %.2f" % (average()))

        case 3:
            print(f"\nInfo: {factorial.__doc__}")
            n = int(input("\nEnter a number: "))
            print(f"Result: {factorial(n)}")

        case 4:
            if arr_dim == None:
                print("\nFirst insert an array.")
                continue
            print(f"\nInfo: {'Filters and displays elements above a threshold.'}")
            threshold = int(input("\nEnter threshold: "))
            filtered = []
            if arr_dim == "1d":
                for ele in arr1:
                    if ele >= threshold:
                        filtered.append(ele)
            else:
                for row in arr2:
                    for ele in row:
                        if ele >= threshold:
                            filtered.append(ele)
            print(f"\nElements >= {threshold}: {filtered}")

        case 5:
            if arr_dim == None:
                print("\nFirst insert an array.")
                continue
            print(f"\nInfo: {'Sorts the active dataset in chosen order.'}")
            print("1. Ascending\n2. Descending") 
            sort_choose = int(input("Choice: ")) 
            if arr_dim == "1d":
                arr1.sort(reverse=(sort_choose == 2))
                print(f"Sorted: {arr1}")
            else:
                sorted_2d = sorted(arr2, key=lambda x: x, reverse=(sort_choose == 2))
                print(f"Sorted Matrix: {sorted_2d}")

        case 6:
            if arr_dim == None:
                print("\nFirst insert an array.")
                continue
            print(f"\nInfo: {data_stat.__doc__}")
            d_min, d_max, d_sum, d_avg = data_stat("Dataset Analysis Report", precision=3)
            
            print(f"Minimum Value : {d_min}")
            print(f"Maximum Value : {d_max}")
            print(f"Total Sum     : {d_sum}")
            print(f"Average Value : {d_avg:.3f}")

        case 0:
            print("Thank You, See You Again 👋")
            break
        
        case _:
          print("Invalid Choice Entered. 🚫")