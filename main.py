from stats import *
from storage import *
print("=================Study Tracker by bluecat-py=================")

def main():
    report = load_report()
    while True:
        print("1. Log study\n2. View report\n3. RESET\n4. EXIT")
        action = input("Choose which action you would like to perform(1-3)\n")

        #responses to the input
        if action == "1": 
            if has_subject(report) == False:
                handle_empty_subject(report)

            elif has_subject(report): #if the subject already exist
                show_subjects(report)
                handle_subject_input(report, input_subject())


        elif action == "2":
            show_study_report(report)
            show_study_log(report)

        elif action == "3":
            reset_report(report)


        elif action == "4":
            save_report(report)
            break

        else:
            print("\nError: Choose the availabe action (1-3)\n")

main()

#TODO: handle invalid input in variable minute
#TODO: simplify average session from this Average Session:  36.333333333333336 to Average Session:  36.33
#TODO: handle an error for when user input only digits(no alphabet) in subject input
#TODO: handle an empty input
#TODO: add remove subject
#PROBLEM: it seems that the program will be in an infinite loop if the user chose a subject which name is in digit
#SOLUTION: I need to format the user's input
#TODO: tell user that the log will only be saved after Exitting the program