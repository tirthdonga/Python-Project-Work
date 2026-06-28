import datetime, time

def current_time():
   date_time = datetime.datetime.now()
   date = date_time.strftime("%d/%m/%Y")
   time = date_time.time().replace(microsecond=0)

   print(f"Current Date = {date}")
   print(f"Current Time = {time}")

def date_difference():
  
   date_str1 = input("Enter The First Date (DD/MM/YYYY): ")
   date_str2 = input("Enter The Second Date (DD/MM/YYYY): ")

   date_1 = datetime.datetime.strptime(date_str1, "%d/%m/%Y").date()
   date_2 = datetime.datetime.strptime(date_str2, "%d/%m/%Y").date()

   gape = date_2 - date_1

   print(f"Difference is: {gape.days}")

def formate_date():
   while True:
      print("\nHere Are The Fomrate Choice: ")
      print("1. DD/MM/YYYY")
      print("2. YYYY/MM/DD")
      print("0. Exit\n")
      choice = int(input("Enter Your Choice: "))
      print()

      match choice:
         case 1: 
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            print(f"Your Formate Is This: {date}")
         case 2: 
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            print(f"Your Formate Is This: {date}")
         case 0: 
            break
         case _:
            print("Invalid Choice Entered 🚫")

def stop_watch():
   print("Press Enter To Start The Stopwatch")
   input()
    
   start_time = time.time()
   print("Stopwatch Started! Press Ctrl+C To Stop.")
    
   try:
      while True:
         elapsed_time = int(time.time() - start_time)
         print(f"Elapsed Time: {elapsed_time} Seconds", end="\r")
         time.sleep(1)
            
   except KeyboardInterrupt:
      print(f"\nStopwatch Stopped. Total Time: {elapsed_time} Seconds")


def count_down():
   start = int(input("Enter The Count-Down Start: "))

   for i in range(start, 0, -1):
      print(f"{i}", end="\r")
      time.sleep(1)
   print("Time Up!")

