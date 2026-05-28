student_list = []
student_dict = {}
all_student_subject = set()

while True:
    print("----------------------------------")
    print("Welcome To Student Data Organizer")
    print("----------------------------------")

    print("\n1. Add Students")
    print("2. Display All Student Information")
    print("3. Display A Student Information")
    print("4. Update Student Infomation")
    print("5. Delete A Student")
    print("6. Clear All Data")
    print("7. Display Subjects Offered")
    print("0. Exit\n")

    choice = int(input("Enter Your choice: "))
    print()

    match choice:
        case 1: 
            print("--------------------")
            print("Enter Student Detail")
            print("--------------------")

            id = int(input("\nEnter Student GRID: "))
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            grade = input("Enter Student Grade: ")
            dob = input("Enter Student DOB (YYYY-MM-DD): ")
            subject = input("Enter Student Subject: ")

            id_tuple = (id)
            dob_tuple = (dob)

            single_subject = []
            raw_subject = subject.split(",")
            
            for s in raw_subject:
                clean_s = s.strip()
                if clean_s != "":
                    single_subject.append(clean_s)
                    all_student_subject.add(clean_s)

            student_info = {'id': id_tuple, 'name': name, 'age': age, 'grade': grade, 'dob': dob_tuple, 'subject': single_subject}

            student_dict[id] = student_info
            student_list.append(student_info)
            print("\nStudent Added Successfully\n")      

        case 2: 
            print("-------------------------")
            print("Displaying All Students  ")
            print("-------------------------")
            
            if not student_list:
                print("\nNo Student Record Found 🚫\n")
            else:
                print()
                for student in student_list:
                    s_id = student['id']
                    s_dob = student['dob']
                    subject_str = ", ".join(student['subject'])
                    print(f"ID: {s_id} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']} | DOB: {s_dob} | Subject: {subject_str}")
                print()

        case 3:
            print("-------------------------")
            print("Search Student Record    ")
            print("-------------------------")

            grid = int(input("\nEnter The ID: "))

            if grid in student_dict:
                student = student_dict[grid]
                
                s_id = student['id']
                s_dob = student['dob']
                subject_str = ", ".join(student['subject'])
                
                print("\n-----------------")
                print("  Student Found  ")
                print("-----------------")
                print(f"ID: {s_id} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']} | DOB: {s_dob} | Subject: {subject_str}\n")
            else:
                print(f"\nStudent Record with ID {grid} Not Found!!\n")

        case 4: 
            print("-------------------------")
            print("Update Student Information")
            print("-------------------------")

            grid = int(input("\nEnter Student ID: "))
            
            if grid in student_dict:
                print("\n-----------------")
                print("   Update Menu   ")
                print("-----------------")
                
                while True:
                    print("\n1. Update Name")
                    print("2. Update Age")
                    print("3. Update Grade")
                    print("4. Update Subjects")
                    print("0. Exit\n")

                    num = int(input("Enter Your Choice: "))

                    match num:
                        case 1: 
                            new_name = input("\nEnter New Name: ")
                            student_dict[grid]['name'] = new_name
                            print("\nName Updated Successfully👍")

                        case 2:
                            new_age = int(input("\nEnter New Age: "))
                            student_dict[grid]['age'] = new_age
                            print("\nAge Updated Successfully👍")

                        case 3:
                            new_grade = input("\nEnter New Grade: ")
                            student_dict[grid]['grade'] = new_grade
                            print("\nGrade Updated Successfully👍")

                        case 4:
                            new_subject = input("\nEnter New Subjects: ")
                            new_single_subject = []
                            new_raw_subject = new_subject.split(",")
                        
                            for s in new_raw_subject:
                                if s != "":
                                    new_single_subject.append(s)
                                    all_student_subject.add(s)
                            student_dict[grid]['subject'] = new_single_subject
                            print("\nSubject Updated Successfully👍")

                        case 0: 
                            print()
                            break
                        case _: 
                            print("\nInvalid Choice Entered!!")
            else:
                print(f"\nStudent Record with ID {grid} Not Found!!\n")

        case 5: 
            print("-------------------------")
            print("Delete Student Record    ")
            print("-------------------------")

            grid = int(input("\nEnter Student ID To Delete: "))

            if grid in student_dict:
                for student in student_list:
                    if student['id'] == grid:
                        student_list.remove(student)
                        break

                del student_dict[grid]
                print("\nStudent Deleted Successfully👍\n")
            else:
                print("\nStudent Record Not Found🚫\n")

        case 6:
            print("-------------------------")
            print("Wipe System Records Data ")
            print("-------------------------")

            print('\nEnter "yes" To Clear All Data')
            print('Enter "no" To Stop\n')
            confirm = input("Enter Your Choice: ")

            if confirm == "yes":
                student_list.clear()
                student_dict.clear()
                all_student_subject.clear()
                print("\nAll Record has Been Cleared🧹\n")
            elif confirm == "no":
                print("\nStoping Exicution🚫\n")
            else:
                print("\nInvalid Choice Entered🚫\n")

        case 7: 
            print("-------------------------")
            print("Display Offered Subjects ")
            print("-------------------------")

            if not all_student_subject:
                print("\nNo Subject Found\n")
            else:
                subjects = ", ".join(all_student_subject)
                print(f"\nAll Unique Subjects: {subjects}\n")

        case 0:
            print("Thank you for using Student Data Organizer! Goodbye! 👋\n")
            break

        case _: 
            print("Invalid Number Entered🚫\n")