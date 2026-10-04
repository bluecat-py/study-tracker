from stats import *
from storage import *
print("=================Study Tracker by bluecat-py=================")

def main():
    report = load_report()
    while True:
        print("1. Log study\n2. View report\n3. Delete subject\n4. RESET\n5. EXIT")
        action = input("Choose which action you would like to perform(1-5)\n")

        #responses to the input
        if action == "1": 
            if has_no_subject(report):
                handle_empty_subject2(report)
            else: #if the subject already exist
                show_subjects(report)
                sub_input = input("\nChoose which subject to record or create a new one\n")
                if isOnlyNumber(sub_input): #scenario 1: user entered number
                    sub_input = int(sub_input) #convert it into integer for comparing
                    if sub_input > len(report) or sub_input == 0 : #if the input is invalid
                        print("No subject matches that number. Enter a valid subject number or type a new subject name to create it.")
                        continue #the code below won't run if the expression is True
                    report[sub_input-1]["minutes"].append(input_minute())
                    print("\nYour study has been recorded...")
                    print("=====================================")
                elif not isOnlyNumber(sub_input): #scenario 2: user entered alphabet
                    found = False
                    for i in range(0, len(report)):
                        if sub_input == report[i]["subject"]: #if the input match with the value in "subject" on i index
                            found = True
                            report[i]["minutes"].append(input_minute())
                            break
                    if found == False: #if no match is found
                        print(f"Subject {sub_input} has been created")
                        report.append(create_subject(sub_input, input_minute()))
                        print("\nYour study has been recorded...")
                        print("=====================================")




        elif action == "2":
            show_study_report(report)
            show_study_log(report)

        elif action == "3":
            delete(report, input("What subject would you like to delete?\n"))
            print("\nSubject deleted.\n")

        elif action == "4":
            reset_report(report)


        elif action == "5":
            save_report(report)
            break

        else:
            print("\nError: Choose the availabe action (1-5)\n")


main()

#TODO: handle an error for when user input only digits(no alphabet) in subject input
#TODO: handle an empty input in "Choose a subject or input a new one" section
#TODO: a user cannot just input "1" for their subject name, because that would be confusing
#TODO: a glitch occur when "You haven't input anything, try again" and you input a valid subject name.
#TODO: only spaces input (  ) should not be permitted. I think strip() can handle this.