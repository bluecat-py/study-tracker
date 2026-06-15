from stats import *
from storage import *
print("=================Study Tracker by bluecat-py=================")

def main():
    #declaring important variable
    report = load_report()
    while True:

        #ask user the action to perform
        print("1. Log study\n2. View report\n3. EXIT")
        action = input("Choose which action you would like to perform(1-3)\n")

        #responses to the input
        if action == "1": 
            if len(report) == 0: #if no subject has been added yet
                sub_input = input("\nIt seems that you haven't added any subject, go ahead and add one.\nSubject: ")
                minute = int(input("Enter study time (minutes): ")) #TODO: make this a function
                report.append(create_subject(sub_input, minute))
                print("\nYour study has been recorded...")
                print("=====================================")
            else: #if the subject already exist
                for i in range(0, len(report)):
                    print(f"{i+1}. {report[i]["subject"]}")
                sub_input = input("\nChoose which subject to record or create a new one\n")
                if isNumber(sub_input): #scenario 1: user entered number
                    sub_input = int(sub_input) #convert it into integer for comparing
                    if sub_input > len(report) or sub_input == 0: #if the input is invalid
                        print("No subject matches that number. Enter a valid subject number or type a new subject name to create it.")
                        continue #the code below won't run if the expression is True
                    minute = int(input("Enter study time (minutes): "))
                    report[sub_input-1]["minutes"].append(minute)
                    print("\nYour study has been recorded...")
                    print("=====================================")
                elif not isNumber(sub_input): #scenario 2: user entered alphabet
                    found = False
                    for i in range(0, len(report)):
                        if sub_input == report[i]["subject"]: #if the input match with the value in "subject" on i index
                            found = True
                            minute = int(input("Enter study time (minutes): "))
                            report[i]["minutes"].append(minute)
                            break
                    if found == False: #if no match is found
                        print(f"Subject {sub_input} has been created")
                        minute = int(input("Enter study time (minutes): "))
                        report.append(create_subject(sub_input, minute))
                        print("\nYour study has been recorded...")
                        print("=====================================")




        elif action == "2":
            show_study_report(report)
            show_study_log(report)


        elif action == "3":
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