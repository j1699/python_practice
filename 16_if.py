while True:
    a = str(input("수강 중인 교과목을 입력해주세요: "))
    if a == "회로이론":
        print("기말고사는 15일 17시에 시작합니다.")
    elif a == "논리회로":
        print("기말고사는 21일 15시에 시작합니다.")
    elif a == "신재생에너지실험":
        print("기말고사는 과제대체입니다.")
    elif a == "명저읽기":
        print("기말고사는 13일 12시에 시작합니다.")
    elif a == "전기기기":
        print("기말고사는 15일 13시에 시작합니다.")
    elif a == "데통네":
        print("기말고사는 17일 12시에 시작합니다.")
    elif a == "종료":
        print("이용해 주셔서 감사합니다.")
        break
    else:
        print("올바른 교과목명을 입력해주세요.")