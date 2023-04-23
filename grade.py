GRADE_POINTS = {'A+': 4.5, 'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5, 'C': 2.0, 'D+': 1.5, 'D': 1.0, 'F': 0.0}
# 계산 함수
# 입력 받은 정보를 저장할 변수들
dictionary = {}
num_input = 0
subject_list = []

# 입력 함수
def Dictionary(subject):
    global num_input
    dictionary[num_input] = subject
    num_input += 1

def Tuple(name, grade, result):
    return (name, grade, result)

def List(n, g, r):
    global subject_list
    subject_list.append(Tuple(n, g, r))

def Input():
    print("과목명을 입력하세요 : ")
    name = input()
    Dictionary(name)

    print("학점을 입력하세요 : ")
    grade = input()

    print("평점을 입력하세요 : ")
    result = input()

    List(name, grade, result)
    print("입력되었습니다.")

# 출력 함수
def Print(submission=False):
    global subject_list
    global dictionary
    for num_input in dictionary:
        if submission:
            if subject_list[num_input][1] != 'F':
                print("[%s] %s학점: %s" % (dictionary[num_input], subject_list[num_input][1], subject_list[num_input][2]))
        else:
            print("[%s] %s학점: %s" % (dictionary[num_input], subject_list[num_input][1], subject_list[num_input][2]))

# 계산 함수
def Calculate(submission=False):
    global subject_list
    global GRADE_POINTS
    total_grade = 0
    total_credit = 0
    for item in subject_list:
        grade = GRADE_POINTS.get(item[1], 0)
        credit = 0
        try:
            credit = float(item[2])
        except ValueError:
            grade = 0

        if submission and grade == 0:
            continue
        total_grade += grade * credit
        total_credit += credit
    if total_credit > 0:
        print("총 학점: %.1f" % total_credit)
        print("평균 평점: %.2f" % (total_grade / total_credit))
    else:
        print("입력된 과목이 없거나 학점 정보가 없습니다.")

# 메인 함수
while True:
    print("작업을 선택하세요.")
    print("1. 입력")
    print("2. 출력")
    print("3. 계산")
    num = int(input())
    if num == 1:
        Input()
    elif num == 2:
        Print(False)
    elif num == 3:
        Calculate(True)
        Calculate(False)
    else:
        print("잘못된 입력입니다. 다시 시도해주세요.")
