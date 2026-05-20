while True:
  print("\n----------------------------------------------------")
  print("Welcome To The Pattern Genrator and Number Analyzer")
  print("----------------------------------------------------\n")
  print("Enter 1 To Generate Pattern")
  print("Enter 2 To Analyze Number")
  print("Enter 0 To Exit\n")

  btn = int(input("Please Enter Number(1, 2, 0): "))
  print()

  match btn:
    case 1: # For Pattern Generator
      print("\n-----------------------------")
      print("Welcome To Pattern generator")
      print("-----------------------------\n")
      print("Enter 1 To Generate Right Side Pattern")
      print("Enter 2 To Generate left Side Pattern")
      print("Enter 3 To Generate Middle Side Pattern")
      print("Enter 0 To Exit\n")

      pattern = int(input("Please Enter Number(1, 2, 3, 0): "))

      match pattern:
        
        case 1:
          row = int(input("\nPlease Enter How Many Row You Want: "))
          print("Here is Right Side Pattern\n")
          
          for i in range(1, row + 1):
            for k in range(row - i):
              print(" ", end=(" "))
            for j in range(1, i + 1):
              print("*", end=(" "))
            print()

        case 2:
          row = int(input("\nPlease Enter How Many Row You Want: "))
          print("Here is Left Side Pattern\n")

          for i in range(1, row + 1):
            for j in range(1, i + 1):
              print("*", end=(" "))
            print()

        case 3:
          row = int(input("\nPlease Enter How Many Row You Want: "))
          print("Here is Middle Side Pattern\n")

          for i in range(1, row + 1):
            for k in range(row - i):
              print("", end=(" "))
            for j in range(1, i + 1):
              print("*", end=(" "))
            print()

        case 0:
          continue

        case _:
          print("\n!!Invalid Number Please Try Again!!")

    case 2:
      print("\n--------------------------")
      print("Welcome To Number Analyzer")
      print("--------------------------\n")
      
      num_start = int(input("Enter The Start Number: "))
      end_start = int(input("Enter The End Number: "))
      
      for i in range (num_start, end_start + 1):
        if i % 2 == 0:
          print(i, "is Even")
        else:
          print(i, "is Odd")

      print("\nEnter 1 To Get Sum Of Even Numbers")
      print("Enter 2 To Get Sum Of Odd Numbers")
      print("Enter 3 To Get Sum Of Total Numbers")
      print("Enter 0 Exit\n")

      sum_num = int(input("\nPlease Enter The Number: "))

      match sum_num:
        case 1:
          sum = 0
          for i in range (num_start, end_start + 1):
            if i % 2 == 0:
              sum += i
          print("\nTotal Sum of Even Number is:", sum)
        
        case 2:
          sum = 0
          for i in range (num_start, end_start + 1):
            if i % 2 != 0:
              sum += i
          print("\nTotal Sum Of Odd Number is:", sum)

        case 3:
          sum = 0
          for i in range (num_start, end_start + 1):
            sum += i
          print("\nTotal Sum Of Total Number is:", sum)

        case 0:
          continue

        case _:
          print("\n!!Please Enter Valid Number!!")

    case 0:
      print("Thank You, BYE!!👋👋👋\n")
      break

    case _:
      print("\n!!Invalid Number Enterred")