# 1
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

# 2
# 오프라인 모임 날짜를 정해주는 프로그램을 작성하라.
# 랜덤으로 날짜를 뽑되, 월별 날짜가 다름을 감안하여 28일 이내로 정한다.
# 매월 1일~3일은 제외한다.
from random import randint
offline = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(offline) +"일입니다.")

# 3
# # 사이트별 비밀번호를 만들어주는 프로그램을 작성하라.
# # 도메인만 포함, 처음 만나는 점 이하는 제외, 남은 글자 중 세자리 + 글자 개수 + e 개수 + '!'로 구성
# # 예) http://naver.com -> nav51!
# site = "http://youtube.com"
# domain = site[7:(site.index("."))]
# password = domain[0:3] + str(len(domain)) + str(domain.count("e")) + "!"
# print(password)
#
# url = "http://youtube.com"
# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(domain.count("e")) + "!"
# print("{0}의 비밀번호는 {1} 입니다.".format(url, password))
#
# # 4
# # 댓글 이벤트 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피를 받는다. 추첨 프로그램을 만들어보자.
# # 조건1: 댓글 작성자 총 20명, 아이디는 1~20
# # 조건2: 무작위 추첨, 중복 불가
# # 조건3: random 모듈의 shuffle과 sample 활용
# from random import shuffle, sample
# users = list(range(1, 21))
# shuffle(users)
# winners = sample(users, 4)
# print("당첨자 발표")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("추카포카~~~")

# 5
# 당신은 택시 기사고, 50명의 승객과 매칭 기회가 있다. 총 탑승 승객 수를 구하는 프로그램을 만들자.
# 조건1: 승객별 운행 소요 시간은 5분 ~ 50분 랜덤
# 조건2: 당신은 5분 ~ 15분 사이의 승객만 매칭되어야 한다.
# count = 0
# for candidate in range(1, 51):
#     time = randint(5, 50)
#     if 5 <= time and time <= 15 :
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(candidate, time))
#         count += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(candidate, time))
# print("총 탑승 승객 : {0}".format(count))

# 6
# 표준 체중을 구하는 프로그램을 작성하라.
# 성별에 따른 공식
# 남자 : 키 * 키 * 22
# 여자 : 키 * 키 * 21
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

height = int(input("키를 입력하세요(cm): "))
gender = input("성별를 입력하세요(남/여): ")

def std_weight(height, gender):
    if gender == "남":
        standard = (height/100) * (height/100) * 22
    elif gender == "여":
        standard = (height/100) * (height/100) * 21
    else:
        print("요상한 입력 값입니다.")
    return standard

weight = std_weight(height, gender)
print(round(weight, 2))

# 7
# - X 주차 주간보고 -
# 부서: 이름: 업무 요약
# 1주차부터 5주차까지의 보고서 파일을 만드는 프로그램을 만들라. '1주차.txt', '2주차.txt'...
for num in range(1, 6):
    with open(str(num)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -\n".format(num))
        report_file.write("부서:\t이름:\t업무 요약:")