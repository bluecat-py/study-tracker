import json

FILENAME = "report.json"


def load_report():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    
    except FileNotFoundError:
        return []
    
def save_report(report):
    with open(FILENAME, "w") as file:
        json.dump(report, file, indent=4)

def reset_report(report):
    with open(FILENAME, "w") as file:
        json.dump([], file, indent=4)
    report.clear()
    print("All has been resetted..")
