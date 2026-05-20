print("Welcome to the F1 Diver Data Collector")

name = str(input("\nPlease Enter Your Name:- "))
enter_year = int(input("Please Enter The Year You Entered F1 Sport:- "))
wins = int(input("Please Enter The Number Of Races You Have won:- "))
dnf = int(input("Please Enter The Number of Races You Have Been DNF From:- "))
company = str(input("Please Enter Your Team Name That you have Driven In:- "))
num = int(input("Please Enter Your Diver Number:- "))

print("\nThank you! Here is the information we collected:")
print("\nName: ", name ,"(Type: ", type(name) ,", Memory Address: ", id(name) , ")")
print("Entered Year: ", enter_year ,"(Type: ", type(enter_year) ,", Memory Address: ", id(enter_year) , ")")
print("Total Wins: ", wins ,"(Type: ", type(wins) ,", Memory Address: ", id(wins) , ")")
print("Total DNF: ", dnf ,"(Type: ", type(dnf) ,", Memory Address: ", id(dnf) , ")")
print("Team Raced With: ", company ,"(Type: ", type(company) ,", Memory Address: ", id(company) , ")")
print("Driver Number: ", num ,"(Type: ", type(num) ,", Memory Address: ", id(num) , ")")

total_year = 2026 - enter_year

print("\nYou have diven in F1 for", total_year , "Year From", enter_year , "to 2026")

win_per = (wins*100) / (23*total_year)

print("\nYour win percentage till", enter_year ,"to 2026 is", int(win_per), "%")

dnf_per = (dnf*100) / (23*total_year)

print("\nYour DNF(Disqualified) percentage till", enter_year ,"to 2026 is", int(dnf_per) , "%")

print("\nThank you for using the Personal Data Collector of F1. Goodbye!")