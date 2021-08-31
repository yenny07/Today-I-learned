# if
weather = input("오늘 날씨가 어떤가유? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세용")
elif weather == "미세먼지":
    print("마스크를 챙기세용")
else:
    print("준비물이 필요 업소용")

temp = int(input("기온은 어때요? "))
if 30 <= temp :
    print("나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮네요")
elif 0 <= temp and temp < 10 :
    print("외투를 챙기세요")
else:
    print("너무 추우니 나가지 마세요.")

# for
for waiting_no in range(1, 5): # 1, 2, 3, 4
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["블랙 위도우", "아이언맨", "그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비 되었어유~".format(customer))

# while
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었구요.. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다. ^^7")

person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")

# continue와 break
absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘은 여기까지. {0}은 교무실로 따라와".format(no_book))
    print("{0}야, 책을 읽어봐".format(student))

# 한 줄 for문
# 출석번호가 1 2 3 4 였는데 앞에 100을 붙이기로 함
students = [1,2,3,4,5]
students =[i+100 for i in students]

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "Groot"]
students = [len(i) for i in students]
