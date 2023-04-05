while 1 > 0:
    print("1. 입력")
    print("2. 출력")
    a = int(input())
    total = 0
    total_a = 0
    k = 0
    grade = 0
    if a == 1:
        while True:
            print("학점을 입력하세요.")
            grade = float(input(""))
            total = total + grade
            print("평점을 입력하세요.")
            alpha = input()
            if alpha == "A+":
                alpha = 4.5
            elif alpha == "A":
                alpha = 4.0
            elif alpha == "B+":
                alpha = 3.5
            elif alpha == "B":
                alpha = 3.0
            elif alpha == "C+":
                alpha = 2.5
            elif alpha == "C":
                alpha = 2.0
            elif alpha == "D+":
                alpha = 1.5
            elif alpha == "D":
                alpha = 1.0
            elif alpha == "F":
                alpha = 0.0
            total_a = total_a + alpha
            k = k + 1
            print("중지하시려면 0, 계속하시려면 1을 눌러주세요")
            num = int(input(""))
            gpa = total_a / k
            if num == 0:
                break
    elif a == 2:
        print("제출용: ", total, "학점 (GPA : ", gpa, ")")
    elif a == 0:
        break
    else:
        print("잘못된 입력입니다.")
