def create_sub(subject: str, minute: list[int]):
    report = {"subject" : subject,
              "minute" : [minute]}
    return report

def isNumber(input):
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    notNumber = 0
    for char in input:
        if char not in number:
            notNumber = 1
    if notNumber == 0:
        return True
    else:
        return False
