import date_time, mathemetic, random_num, file_op, uuid_gene, dir_modul

while True:
  print("=" * 40)
  print("Welcome To Multi-Utility Toolkit")
  print("=" * 40)
  print("Choose An Option:")
  print("1. Date-Time And Time Operation")
  print("2. Mathemetical Operation")
  print("3. Random Data Generation")
  print("4. Generate Unique Identifiers (UUID)")
  print("5. File Operations (Custome Module)")
  print("6. Explore Module Atrribute dir()")
  print("0. Exit")
  print("=" * 40)
  choice = int(input("Enter Your Choice: "))

  match choice:
    case 1: 
      while True:
        print("\nDate-Time And Time Operation")
        print("1. Display Current Date And Time")
        print("2. Calculate Difference Between Two Dates/Time")
        print("3. Formate Date Into Custome Format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("0. Back To Main Menu\n")
        sub_choice1 = int(input("Enter Your Choice: "))
        print()

        match sub_choice1:
          case 1:
            date_time.current_time()
            print()
          case 2: 
            date_time.date_difference()
          case 3: 
            date_time.formate_date()
          case 4: 
            date_time.stop_watch()
          case 5: 
            date_time.count_down()
          case 0: 
            break
          case _: 
            print("Invalid Choice Entered 🚫")

    case 2:
      while True:
        print("\nMethemetical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculation")
        print("4. Aria Of GEomatric Shape")
        print("0. Back To Main Menu\n")
        sub_choice2 = int(input("Enter Your Choice: "))
        print()

        match sub_choice2:
          case 1: 
            mathemetic.cal_factorial()
          case 2: 
            mathemetic.compound_interest()
          case 3: 
            mathemetic.Trigonometri()
          case 4: 
            mathemetic.calculate_area()
          case 0: 
            break
          case _:
            print("Invalid Choice Entered")

    case 3: 
      while True:
        print("\nRandom Data Generations:")
        print("1. Generate Random Number")
        print("2. Generate Randome List")
        print("3. Create Random Password")
        print("4. Generate Randome OTP")
        print("0. Back To Main Menu\n")
        sub_choice3 = int(input("Enter Your Choice: "))
        print()

        match sub_choice3:
          case 1: 
            random_num.random_num()
          case 2: 
            random_num.random_list()
          case 3: 
            random_num.generate_password()
          case 4: 
            random_num.generate_otp()
          case 0: 
            break
          case _:
            print("Invalid Choice Entered!!")

    case 4:
      uuid_gene.generate_uuid()
    case 5: 
      while True:
        print("\nFile Operations:")
        print("1. Create A New File")
        print("2. Write To A File")
        print("3. Read From A File")
        print("4. Append To A File")
        print("0. Back To Main Menu\n")
        sub_choice4 = int(input("Enter Your Choice: "))
        print()

        match sub_choice4:
          case 1: 
            file_op.create_file()
          case 2: 
            file_op.write_file()
          case 3: 
            file_op.read_file()
          case 4: 
            file_op.append_file()
          case 0:
            break
          case _: 
            print("Invalid Choice Entered!!")

    case 6: 
      dir_modul.module_attributes()
    case 0: 
      break
    case _:
      print("Invalid Choice Entered!!!")