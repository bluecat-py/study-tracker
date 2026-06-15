def format_time(total_minute: int): 
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
    print(f"Total Study Time: {calculate_study_report(report)[2]}")

def show_study_log(report):
    for i in range(0, len(report)):
        print("\n"+report[i]["subject"].capitalize())
        print("==================================================")
        print(f"Sessions: {calculate_subject_report(report)[i]["total sessions"]}")
        print(f"Total Time Spent: {calculate_subject_report(report)[i]["total time spent"]}")
        print(f"Average Session:  {calculate_subject_report(report)[i]["average session"]}")
        for minute in range(0, len(report[i]["minutes"])):
            print(f"Session {minute+1}: {report[i]["minutes"][minute]}\n")




