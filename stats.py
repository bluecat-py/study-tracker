#formatting
def format_time(total_minute): 
    hour_digits = []
    hours_as_strings = str(total_minute / 60) #so I can iterate it
    for num in hours_as_strings:
        if num == ".":
            break #to stop when it found a dot
        else:
            hour_digits.append(num) #or I can just use //
    hour = str(".".join(hour_digits)) + "h"
    minute = str(total_minute % 60) +"m"
    return hour + " " + minute
        
def create_subject(subject: str, minutes: list[int]):
    report = {"subject" : subject,
              "minutes" : [minutes]}
    return report

def isNumber(value: str) -> bool:
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    notNumber = 0
    for char in value:
        if char not in number:
            notNumber = 1
    if notNumber == 0:
        return True
    else:
        return False

def isOnlyNumber(value: str) -> bool:
    NumCount = 0
    for char in value:
        if isNumber(char): #PROBLEM: This line is trying to iterate an iteration
            NumCount += 1
    if NumCount == len(value):
        return True
    else:
        return False

#input logic
def input_subject():
    try:
        subject_input = input("\nChoose which subject to record or create a new one\n")
    except isOnlyNumber(subject_input):
        raise ValueError("A subject cannot be only digit numbers")


def input_minute():
    while True:
        try:
            minute = int(input("Enter study time (minutes): "))
            break
        except ValueError:
            print("Please enter minutes in digit numbers.\n")
    return minute

def has_subject(report):
    if len(report) > 0:
        return True
    else:
        return False

def record_new_subject(report: list[dict], subject_input: str): #TODO: it seems that the program will be in an infinite loop if the user chose a subject which name is in digit
    while True:
        if subject_input == "": #suppose user typed nothing
            subject_input = input("You haven't typed anything, try again.\nSubject: ")
        else:
            minute = input_minute()
            break
    report.append(create_subject(subject_input, minute))
    print("\nYour study has been recorded...")
    print("=====================================")

def record_subject(report, subject_input):
    if isNumber(subject_input):
        subject_input = int(subject_input)
        minute = input_minute()
        report[subject_input - 1]["minutes"].append(minute)
    else:
        minute = input_minute()
        report[subject_exist(report, subject_input)[1]]["minutes"].append(minute)
        

def subject_exist(report, subject_input):  #TODO: it seems that the program will be in an infinite loop if the user chose a subject which name is in digit
    subject = None
    found = False
    if isNumber(subject_input):
        subject_input = int(subject_input)
        if subject_input > len(report) or subject_input == 0:
            found = False
        else:
            found = True
    elif isNumber(subject_input) == False:
        for i in range(0, len(report)):
            if subject_input in report[i]["subject"]:
                found = True
                subject = i
                break
    return found, subject


def handle_empty_subject(report):
    subject_input = input("\nIt seems that you haven't added any subject, go ahead and add one.\nSubject: ")
    record_new_subject(report, subject_input)

def show_subjects(report):
    for i in range(0, len(report)):
        print(f"{i+1}. {report[i]["subject"]}")
    
def handle_subject_input(report, subject_input):
    while True:
        if subject_exist(report, subject_input)[0] == False:
            print("No subject matches that number. Enter a valid subject number or type a new subject name to create it.")
        elif subject_exist(report, subject_input)[0] == True:
            record_subject(report,subject_input)
            break
        else:
            record_new_subject(report, subject_input)
            break


#calculation
def calculate_study_report(report: list[dict]) -> list[int, int, str]:
    total_subjects = len(report)
    total_sessions = 0
    total_study = 0
    for i in range(0, len(report)):
        total_sessions += len(report[i]["minutes"])
        for minute in report[i]["minutes"]:
            total_study += minute
    total_study = format_time(total_study)
    return total_subjects, total_sessions, total_study

def calculate_subject_report(report):
    study_log_report = []
    total_sessions, total_time_spent, average_session = 0, 0, 0
    for i in range(0, len(report)):
        for minute in report[i]["minutes"]:
            total_time_spent += minute
        total_sessions = len(report[i]["minutes"])
        average_session = total_time_spent / total_sessions
        subject = report[i]["subject"]
        study_log_report.append(
            {
            "subject": subject,
            "total sessions": total_sessions,
            "total time spent": total_time_spent,
            "average session": average_session,
            }
        )
    return study_log_report


#presentation
def show_study_report(report):
    print("================== STUDY REPORT ==================\n")
    print(f"Subjects: {calculate_study_report(report)[0]}")
    print(f"Total Sessions: {calculate_study_report(report)[1]}")
    print(f"Total Study Time: {calculate_study_report(report)[2]}\n")

def show_study_log(report): 
    for i in range(0, len(report)):
        print("\n"+report[i]["subject"].capitalize())
        print("==================================================")
        print(f"Sessions: {calculate_subject_report(report)[i]["total sessions"]}")
        print(f"Total Time Spent: {calculate_subject_report(report)[i]["total time spent"]}")
        print(f"Average Session:  {calculate_subject_report(report)[i]["average session"]}")
        for minute in range(0, len(report[i]["minutes"])):
            print(f"Session {minute+1}: {report[i]["minutes"][minute]}")
        print("==================================================\n")
