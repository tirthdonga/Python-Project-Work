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

def data_stat(*args, **kwargs):
    """Returns min, max, sum, and average, allowing extra args and precision kwargs."""
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
    
    # Example use of kwargs: adjust rounding precision
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
    print("1. Insert Data as an array\n2. Display Data Summary\n3. Calculate Factorial\n4. Filter Data By Threshold\n5. Sort Data\n6. Display Dataset Statistics\n0. Exit")
    choice = int(input('\nEnter your choice: '))
    
    match choice:
        case 1:
            choice_dim = int(input("\n1. 1D Array\n2. 2D Array\nChoice: "))
            choice_src = int(input("1. Sample\n2. Manual\nChoice: "))
            if choice_dim == 1:
                sample_1d() if choice_src == 1 else manual_1d(input("Numbers: "))
            else:
                sample_2d() if choice_src == 1 else manual_2d(int(input("Rows: ")))

        case 2:
            if arr_dim == None:
                continue
            if arr_dim == "1d":
                print(f"Min: {min(arr1)}, Max: {max(arr1)}, Sum: {sum(arr1)}, Avg: {sum(arr1)/len(arr1):.2f}")
            else:
                print(f"Min: {minimum()}, Max: {maximum()}, Sum: {total_sum()}, Avg: {average():.2f}")

        case 3:
            n = int(input("\nEnter number: "))
            print(f"Result: {factorial(n)}")

        case 4:
            if arr_dim == None: continue
            threshold = int(input("Threshold: "))
            data = arr1 if arr_dim == "1d" else [x for row in arr2 for x in row]
            print([x for x in data if x >= threshold])

        case 5:
            if arr_dim == None: continue
            rev = int(input("1. Asc\n2. Desc\nChoice: ")) == 2
            if arr_dim == "1d": arr1.sort(reverse=rev); print(arr1)
            else: [row.sort(reverse=rev) for row in arr2]; print(arr2)

        case 6:
            if arr_dim == None: continue
            # Calling with *args (e.g., a custom label) and **kwargs (precision)
            d_min, d_max, d_sum, d_avg = data_stat("StatReport", precision=3)
            print(f"\nMin: {d_min}, Max: {d_max}, Sum: {d_sum}, Avg: {d_avg:.3f}")

        case 0:
            break